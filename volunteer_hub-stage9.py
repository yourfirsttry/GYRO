# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: VolunteerHub
import json, sys

INITIAL_DATA = '''
{
    "participants": [
        {"id": 1, "name": "Алексей", "email": "alex@example.com"},
        {"id": 2, "name": "Мария", "email": "maria@example.com"}
    ],
    "events": [
        {"id": 101, "title": "Помощь в приюте", "date": "2024-10-25T10:00:00"},
        {"id": 102, "title": "Сбор гуманитарной помощи", "date": "2024-10-27T14:00:00"}
    ],
    "shifts": [
        {"event_id": 101, "participant_id": 1, "role": "Координатор"},
        {"event_id": 101, "participant_id": 2, "role": "Волонтер"}
    ]
}'''

def load_initial_data():
    try:
        return json.loads(INITIAL_DATA)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга начальных данных: {e}")
        sys.exit(1)

if __name__ == "__main__":
    data = load_initial_data()
    for p in data["participants"]:
        print(f"Участник: {p['name']}")
    for e in data["events"]:
        print(f"Событие: {e['title']} ({e['date']})")
