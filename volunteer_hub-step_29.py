# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: VolunteerHub
# VolunteerHub — Этап 29: Конфигурация через словарь настроек
APP_CONFIG = {
    "name": "VolunteerHub",
    "version": "0.1",
    "language": "ru",
    "max_volunteers_per_shift": 5,
    "default_shift_hours": 4,
    "report_email": "",
    "events_calendar_url": "",
}

def get_config(key: str = None):
    if key is None:
        return APP_CONFIG.copy()
    return APP_CONFIG.get(key)
