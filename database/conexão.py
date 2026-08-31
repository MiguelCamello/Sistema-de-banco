from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).parent.parent
PASTA_DATA = BASE_DIR / "data"
PASTA_DATA.mkdir(parents=True, exist_ok=True)
BANCO = PASTA_DATA / "banco.db"

def conectar():
    return sqlite3.connect(BANCO)