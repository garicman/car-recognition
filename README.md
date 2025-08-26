# Car Recognition — Archived Notebook

This repository preserves an older machine-learning project for **car brand recognition**.
It contains the original Jupyter notebook and minimal scaffolding so it’s easy to run and archive.

- **Main artifact:** `notebooks/01_car_recognition_demo.ipynb`
- **Status:** Archived / read-only
- **Owner:** Martin Garic

## Dataset layout (your data)
You mentioned two dataset variants on disk:

- `2brands/` — two subfolders, each corresponding to **one car brand** (binary classification).
- `3brands/` — three subfolders: two specific brands **plus** a folder with **random brands** (treated as an **'other'** class).

These folders are classic *ImageFolder* style (one directory per class). If you want train/val/test splits,
use the helper script below to create split copies.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# (Optional) launch Jupyter to run the original notebook
python -m pip install jupyterlab
jupyter lab
```

Open `notebooks/01_car_recognition_demo.ipynb` and update the data paths to point to **your local** `2brands/` or `3brands/` folders.

## Optional: create train/val/test splits
If your raw folders have only class subfolders without splits, you can generate split directories:

```bash
python scripts/prepare_splits.py \
  --source /path/to/2brands \
  --out ./data/2brands_split \
  --val-ratio 0.15 --test-ratio 0.15 --seed 42

# Result: data/2brands_split/{{train,val,test}}/{{class_name}}/...
```

Repeat for `3brands` if needed.

## Notes
- This repo keeps the **original notebook** for posterity; it may not reflect current best practices.
- Data is **not** included; use your local copies.
- If you later add trained weights or large results, consider Git LFS.

## License
MIT — see [LICENSE](LICENSE).
