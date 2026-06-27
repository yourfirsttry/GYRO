# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: VolunteerHub
import json, os
from typing import List, Dict, Optional

def load_data_from_file(file_path: str) -> tuple[Optional[List], Optional[str]]:
    if not os.path.exists(file_path):
        return [], f"Файл не найден: {file_path}"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data, None
        elif isinstance(data, dict):
            # Если файл содержит объект с ключами (например, "participants"), возвращаем список значений или пустой список
            values = list(data.values()) if len(data) > 0 else []
            return values, None
        else:
            return [], "Неверный формат JSON данных"
    except json.JSONDecodeError as e:
        return [], f"Ошибка парсинга JSON: {e}"
    except Exception as e:
        return [], f"Произошла неизвестная ошибка при чтении файла: {e}"

# Пример вызова (раскомментируйте для использования):
# participants, error = load_data_from_file("volunteers.json")
# if not error and participants: print(f"Загружено участников: {len(participants)}")
