import sys
from pathlib import Path

def txt_importer(file_path):
    path = Path(file_path)
    
    if not file_path.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
        return []

    if not path.exists():
        sys.stderr.write(f"Arquivo {file_path} não encontrado\n")
        return []

    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
        return lines
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {file_path} não encontrado\n")
        return []
    