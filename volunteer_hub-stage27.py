# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: VolunteerHub
def reset_demo_data():
    """Сбрасывает все сущности в начальные демо-данные."""
    global _events, _shifts, _participants, _reports, _tasks

    _events = [
        {"id": 1, "title": "Волонтёрский марафон", "date": "2025-03-15", "capacity": 50},
        {"id": 2, "title": "Экологическая акция", "date": "2025-04-20", "capacity": 20},
    ]

    _shifts = [
        {"id": 1, "event_id": 1, "start_time": "09:00", "end_time": "13:00"},
        {"id": 2, "event_id": 1, "start_time": "14:00", "end_time": "17:00"},
        {"id": 3, "event_id": 2, "start_time": "10:00", "end_time": "15:00"},
    ]

    _participants = [
        {"id": 1, "name": "Анна Иванова", "email": "anna@example.com", "phone": "+79001112233", "available_shifts": 4},
        {"id": 2, "name": "Борис Петров", "email": "boris@example.com", "phone": "+79004445566", "available_shifts": 3},
    ]

    _tasks = []
    _reports = []


def clear_all_state():
    """Полностью очищает все данные и сбрасывает глобальные переменные."""
    global _events, _shifts, _participants, _reports, _tasks

    _events = []
    _shifts = []
    _participants = []
    _reports = []
    _tasks = []


reset_demo_data()
