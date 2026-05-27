#!/usr/bin/env python3
import glob
from pathlib import Path
from PIL import Image
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
FINAL_DIR = ROOT / "assets" / "ponchi" / "final"

def audit():
    images = glob.glob(str(FINAL_DIR / "*.png")) + glob.glob(str(FINAL_DIR / "*.webp"))
    if not images:
        print(f"No images found in {FINAL_DIR}")
        return

    # 重複を排除 (同名のエントリで png と webp が両方ある場合は png を優先)
    by_stem = {}
    for p_str in sorted(images):
        p = Path(p_str)
        if p.stem not in by_stem or p.suffix == ".png":
            by_stem[p.stem] = p

    sizes = []
    aspect_ratios = []
    
    for stem, path in by_stem.items():
        try:
            with Image.open(path) as im:
                w, h = im.size
                aspect = round(w / h, 2)
                sizes.append((w, h))
                aspect_ratios.append(aspect)
        except Exception as e:
            print(f"Error reading {path.name}: {e}")

    size_counter = Counter(sizes)
    aspect_counter = Counter(aspect_ratios)

    print(f"=== Image Size Audit ===")
    print(f"Total unique entry images scanned: {len(by_stem)}")
    print("\nTop 5 Common Sizes (Width x Height):")
    for size, count in size_counter.most_common(5):
        print(f"  {size[0]}x{size[1]} : {count} images ({count/len(by_stem)*100:.1f}%)")

    print("\nTop 5 Common Aspect Ratios (Width / Height):")
    for aspect, count in aspect_counter.most_common(5):
        print(f"  {aspect:.2f} : {count} images ({count/len(by_stem)*100:.1f}%)")

if __name__ == "__main__":
    audit()
