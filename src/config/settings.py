# Import standard library modules
from pathlib import Path

# The ROOT_DIR should represent the absolute path of the project root folder
ROOT_DIR = Path(__file__).absolute().parent.parent

DATA_DIR = ROOT_DIR / "data"
SQL_DIR = ROOT_DIR / "sql"
