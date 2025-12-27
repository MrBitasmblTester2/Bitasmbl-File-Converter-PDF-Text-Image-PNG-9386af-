from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR/"uploads"
CONVERTED_DIR = BASE_DIR/"converted"
for d in (UPLOAD_DIR, CONVERTED_DIR):
    d.mkdir(exist_ok=True)