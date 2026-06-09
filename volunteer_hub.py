# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: VolunteerHub
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any

# --- Базовая структура данных и точка входа ---

def get_demo_data() -> Dict[str, Any]:
    """Генерирует демонстрационные данные для VolunteerHub."""
    now = datetime.now()
    
    # Участники
    participants: List[Dict[str, Any]] = [
        {"id": 1, "name": "Иван Петров", "email": "ivan@example.com", "skills": ["строительство", "логистика"]},
        {"id": 2, "name": "Анна Сидорова", "email": "anna@example.com", "skills": ["медицина", "первая помощь"]},
        {"id": 3, "name": "Сергей Волков", "email": "sergey@example.com", "skills": ["IT", "связь"]}
    ]
    
    # События
    events: List[Dict[str, Any]] = [
        {
            "id": 101,
            "title": "Помощь в приюте 'Лапки'",
            "date": now + timedelta(days=2),
            "location": "г. Москва, ул. Примерная, 1",
            "description": "Сбор корма и уборка помещений.",
            "slots": 5,
            "filled": 0
        },
        {
            "id": 102,
            "title": "Эко-акция 'Чистый парк'",
            "date": now + timedelta(days=7),
            "location": "Парк Горького",
            "description": "Сбор мусора и высадка деревьев.",
            "slots": 20,
            "filled": 5
        }
    ]
    
    # Смены (связывают участников и события)
    shifts: List[Dict[str, Any]] = [
        {"event_id": 101, "participant_id": 1, "role": "помощник", "status": "confirmed"},
        {"event_id": 102, "participant_id": 3, "role": "координатор", "status": "pending"}
    ]
    
    # Отчёты
    reports: List[Dict[str, Any]] = [
        {"event_id": 100, "author_id": 1, "date": now - timedelta(days=1), 
         "summary": "Успешно завершена уборка в парке. Собрано 5 мешков мусора.", 
         "rating": 5}
    ]
    
    return {
        "participants": participants,
        "events": events,
        "shifts": shifts,
        "reports": reports
    }

def main():
    """Точка входа в приложение."""
    print("=== VolunteerHub: Органайзер волонтёрских задач ===")
    
    # Инициализация данных
    data = get_demo_data()
    
    # Вывод статистики (демонстрация работы с данными)
    total_participants = len(data["participants"])
    total_events = len(data["events"])
    total_shifts = len(data["shifts"])
    
    print(f"Загружено участников: {total_participants}")
    print(f"Доступных событий: {total_events}")
    print(f"Занято смен: {total_shifts}")
    
    # Пример отрисовки ближайшего события
    if data["events"]:
        next_event = min(data["events"], key=lambda x: x["date"])
        print(f"\nБлижайшее событие: {next_event['title']}")
        print(f"Дата: {next_event['date'].strftime('%d.%m.%Y')}")
        print(f"Место: {next_event['location']}")
    
    # Сохранение демо-данных в файл (для последующего использования)
    with open("volunteer_hub_demo.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("\nДемо-данные сохранены в volunteer_hub_demo.json")

if __name__ == "__main__":
    main()
