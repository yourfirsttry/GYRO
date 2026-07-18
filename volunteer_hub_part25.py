# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: VolunteerHub
def validate_date(date_str: str) -> tuple[bool, str]:
    """Проверяет корректность даты в формате YYYY-MM-DD и возвращает (True, "OK") или (False, сообщение об ошибке)."""
    if not isinstance(date_str, str):
        return False, "Дата должна быть строкой"
    
    try:
        parts = date_str.split('-')
        if len(parts) != 3 or len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
            return False, f"Неверный формат даты. Ожидается YYYY-MM-DD"
        
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        
        if year < 1900 or year > 2100:
            return False, f"Год {year} вне допустимого диапазона (1900-2100)"
        
        month_range = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            month_range[1] = 29
        
        if month < 1 or month > 12:
            return False, f"Месяц {month} не существует"
        
        if day < 1 or day > month_range[month - 1]:
            return False, f"День {day} не существует для месяца {month}"
        
        return True, "Дата корректна"
    
    except Exception as e:
        return False, f"Ошибка при проверке даты: {str(e)}"
