import json

from typing import Dict, List, Any


def update_json(data: List[Dict[str, Any]], file_path: str) -> None:
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    except Exception as e:
        print(f"Erro ao salvar dados em {file_path}: {e}")