#!/usr/bin/env python3
import glob
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def search():
    print("=== Searching for 'banana' ===")
    for p_str in glob.glob(str(ROOT / "**/*"), recursive=True):
        p = Path(p_str)
        if p.is_file() and p.suffix in (".py", ".md", ".json", ".yaml", ".yml", ".txt", ".csv", ".sh"):
            try:
                content = p.read_text(encoding="utf-8", errors="ignore")
                if "banana" in content.lower():
                    print(f"Found in: {p.relative_to(ROOT)}")
                    # 該当行を表示
                    for i, line in enumerate(content.splitlines(), start=1):
                        if "banana" in line.lower():
                            print(f"  Line {i}: {line.strip()[:100]}")
            except Exception as e:
                pass

if __name__ == "__main__":
    search()
