#!/usr/bin/env python3
import argparse, random, shutil
from pathlib import Path

def main(source, out, val_ratio, test_ratio, seed):
    random.seed(seed)
    source = Path(source)
    out = Path(out)
    assert source.exists(), f"Source not found: {source}"
    for split in ("train","val","test"):
        (out / split).mkdir(parents=True, exist_ok=True)

    classes = [p for p in source.iterdir() if p.is_dir()]
    for cls in classes:
        images = [p for p in cls.glob("*") if p.is_file()]
        random.shuffle(images)
        n = len(images)
        n_test = int(n * test_ratio)
        n_val = int(n * val_ratio)
        test_set = images[:n_test]
        val_set = images[n_test:n_test+n_val]
        train_set = images[n_test+n_val:]

        for split, subset in (("train", train_set), ("val", val_set), ("test", test_set)):
            dest = out / split / cls.name
            dest.mkdir(parents=True, exist_ok=True)
            for img in subset:
                shutil.copy2(img, dest / img.name)
    print(f"Done. Wrote splits under: {out}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, help="Path to folder with class subfolders (e.g., 2brands or 3brands)")
    ap.add_argument("--out", required=True, help="Output directory for split dataset")
    ap.add_argument("--val-ratio", type=float, default=0.15)
    ap.add_argument("--test-ratio", type=float, default=0.15)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    assert 0 <= args.val_ratio < 1 and 0 <= args.test_ratio < 1 and args.val_ratio + args.test_ratio < 1, "Invalid split ratios"
    main(args.source, args.out, args.val_ratio, args.test_ratio, args.seed)
