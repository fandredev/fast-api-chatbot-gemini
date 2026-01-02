from dotenv import load_dotenv
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT_DIR))

load_dotenv(ROOT_DIR / ".env")
