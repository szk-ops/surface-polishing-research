from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
SYNTHETIC_DIR = DATA_DIR / "synthetic"
PROCESSED_DIR = DATA_DIR / "processed"
RAW_DIR = DATA_DIR / "raw"
MODELS_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"

IMAGE_SIZE = (256, 256)
DEFAULT_SEED = 42

# Example parameter ranges for polishing research
POLISHING_PARAMS = {
    "speed": (1000, 5000),
    "pressure": (0.5, 4.0),
    "feed": (0.1, 2.0),
    "grain_size": (60, 2000),
}
