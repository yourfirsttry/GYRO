# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: VolunteerHub
import json, os

DATA_FILE = "volunteer_hub_data.json"

def save_state(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[ERROR] Не удалось сохранить данные в {DATA_FILE}: {e}")
        return False

def load_state():
    if not os.path.exists(DATA_FILE):
        return {"participants": [], "shifts": [], "events": [], "reports": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Восстановление структуры по умолчанию, если файл повреждён или старый
        for key in ["participants", "shifts", "events", "reports"]:
            if key not in data or not isinstance(data[key], list):
                data[key] = []
        return data
    except Exception as e:
        print(f"[ERROR] Ошибка чтения файла {DATA_FILE}: {e}")
        return {"participants": [], "shifts": [], "events": [], "reports": []}

# Инициализация глобального хранилища при старте программы
if __name__ == "__main__":
    app_data = load_state()
