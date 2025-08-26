# Data Guide

This repository does **not** bundle any images. Point the notebook to your own folders.

## Layouts you described
- `2brands/`
  - `brand_A/` (images)
  - `brand_B/` (images)

- `3brands/`
  - `brand_A/` (images)
  - `brand_B/` (images)
  - `other/`    (images of random brands; this becomes the 'other' class)

## Creating splits
If you only have raw class folders, you can generate train/val/test splits:

```bash
python scripts/prepare_splits.py --source /path/to/2brands --out ./data/2brands_split --val-ratio 0.15 --test-ratio 0.15
```

This will create `data/2brands_split/{{train,val,test}}/{{class}}/...` with copied images.
