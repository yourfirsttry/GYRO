# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: VolunteerHub
class ValidationError(Exception):
    pass

def validate_name(name: str) -> str:
    if not name or len(name.strip()) < 2:
        raise ValidationError("Имя должно содержать от 2 символов")
    return name.strip().title()

def validate_email(email: str) -> str:
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email or not re.match(pattern, email):
        raise ValidationError("Некорректный формат email")
    return email.lower()

def validate_date(date_str: str) -> str:
    try:
        from datetime import datetime
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        raise ValidationError("Дата должна быть в формате YYYY-MM-DD")

def validate_task_duration(hours: float) -> float:
    if hours <= 0 or hours > 24:
        raise ValidationError("Длительность смены должна быть от 1 до 24 часов")
    return round(hours, 1)
