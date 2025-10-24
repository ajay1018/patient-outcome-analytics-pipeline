from pathlib import Path
src = Path("data/raw/patients.csv")
assert src.exists(), "Missing data/raw/patients.csv"
print(f"[extract] found {src} (size={src.stat().st_size} bytes)")
