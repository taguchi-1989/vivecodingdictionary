#!/usr/bin/env python3
"""assets/ponchi/final/ 内のすべての画像をアスペクト比 2:1 に変換し、品質を統一してWebP化する。

- 元画像の端（左上ピクセル）の色をサンプリングし、自然に馴染む背景色として余白部分を塗りつぶします。
- 1254x1254 (1:1) の画像を 1254x627 (2:1) にリサイズ・余白追加します（元画像を627x627に縮小して中央配置）。
  ※ 引数 --high-res を指定すると、元の解像度を維持して 2508x1254 (2:1) にします。
- PNG は 2:1 に上書き保存し、WebP も品質を統一して再生成します。
"""
from __future__ import annotations

import argparse
import glob
import sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
FINAL_DIR = ROOT / "assets" / "ponchi" / "final"


def process_image(img_path: Path, high_res: bool, quality: int) -> bool:
    try:
        with Image.open(img_path) as im:
            # RGBモードに変換 (PNGやWebPのRGBA対応)
            if im.mode not in ("RGB", "RGBA"):
                im = im.convert("RGBA")
            
            orig_w, orig_h = im.size
            
            # 2:1 の新しいキャンバスサイズを決定
            if high_res:
                # 高さを維持して 2508x1254 にする (元画像は 1254x1254 のまま中央配置)
                new_h = orig_h
                new_w = orig_h * 2
                scale_w = orig_w
                scale_h = orig_h
            else:
                # 幅を維持して 1254x627 にする (元画像を 627x627 に縮小して中央配置)
                new_w = orig_w
                new_h = orig_w // 2
                scale_w = new_h
                scale_h = new_h

            # 左上ピクセル (座標 4, 4) から背景色をサンプリングして余白を馴染ませる
            # 端のノイズを避けるため少し内側をサンプリング
            sample_x = min(4, orig_w - 1)
            sample_y = min(4, orig_h - 1)
            bg_color = im.getpixel((sample_x, sample_y))
            
            # アルファチャンネルが不要な場合は RGB キャンバスにする
            if len(bg_color) == 4 and bg_color[3] == 0:
                # 完全に透明な場合は白背景にするか、RGBAで透明キャンバスを作成
                new_canvas = Image.new("RGBA", (new_w, new_h), (255, 255, 255, 0))
            else:
                # 不透明な場合はサンプリングした色で塗りつぶす (RGB化)
                if len(bg_color) == 4:
                    # RGBAの場合はRGBに潰す
                    bg_color_rgb = bg_color[:3]
                else:
                    bg_color_rgb = bg_color
                new_canvas = Image.new("RGB", (new_w, new_h), bg_color_rgb)

            # 元画像を新しいアスペクト比用にリサイズ (アンチエイリアシング高品質)
            resized_im = im.resize((scale_w, scale_h), Image.Resampling.LANCZOS)
            
            # 中央に配置
            paste_x = (new_w - scale_w) // 2
            paste_y = (new_h - scale_h) // 2
            
            # アルファチャンネルがある場合はマスクとして使用して貼り付け
            if resized_im.mode == "RGBA":
                new_canvas.paste(resized_im, (paste_x, paste_y), resized_im)
            else:
                new_canvas.paste(resized_im, (paste_x, paste_y))

            # PNG で保存し直す (元のファイルが PNG の場合、または PNG が存在する場合)
            png_path = img_path.with_suffix(".png")
            
            # RGB または RGBA のまま保存
            new_canvas.save(png_path, "PNG")
            
            # WebP にも保存 (品質とじっくり圧縮パラメータを統一)
            webp_path = img_path.with_suffix(".webp")
            # WebP保存時はRGBに変換してサイズを削減 (透明度がない場合)
            if new_canvas.mode == "RGBA" and not has_transparency(new_canvas):
                save_canvas = new_canvas.convert("RGB")
            else:
                save_canvas = new_canvas

            save_canvas.save(webp_path, "WEBP", quality=quality, method=6)
            
            return True
    except Exception as e:
        print(f"Error processing {img_path.name}: {e}")
        return False


def has_transparency(img: Image.Image) -> bool:
    if img.mode != "RGBA":
        return False
    # アルファ極小値があるかスキャン
    alpha = img.getchannel("A")
    return any(v < 255 for v in alpha.getdata())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--high-res", action="store_true", help="高解像度を維持 (2508x1254)")
    ap.add_argument("--quality", type=int, default=80, help="WebP の圧縮品質 (既定 80)")
    args = ap.parse_args()

    # 重複を避けるため、まず PNG と WebP をすべてリストアップして一意のエントリIDにまとめる
    all_files = glob.glob(str(FINAL_DIR / "*.png")) + glob.glob(str(FINAL_DIR / "*.webp"))
    if not all_files:
        print(f"no images found in {FINAL_DIR}")
        return 0

    stems = sorted(list({Path(p).stem for p in all_files}))
    print(f"Found {len(stems)} entry images to process.")
    print(f"Mode: {'High-res (2508x1254)' if args.high_res else 'Standard (1254x627)'}")
    print(f"WebP Quality: {args.quality}")

    success_count = 0
    for idx, stem in enumerate(stems, start=1):
        # PNG があれば優先的に入力元にする (画質劣化を防ぐため)
        png_path = FINAL_DIR / f"{stem}.png"
        webp_path = FINAL_DIR / f"{stem}.webp"
        
        src_path = png_path if png_path.exists() else webp_path
        
        if process_image(src_path, args.high_res, args.quality):
            success_count += 1
            if idx % 50 == 0 or idx == len(stems):
                print(f"  Processed {idx}/{len(stems)}...")

    print(f"\nSuccessfully unified size (2:1) and quality for {success_count}/{len(stems)} images.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
