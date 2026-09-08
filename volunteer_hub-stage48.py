# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: VolunteerHub
def split_task_duration(task_duration: int, unit: str) -> tuple[int, str]:
    """Разбить длительность задачи на часы и минуты."""
    if unit == "hours":
        return task_duration, "hours"
    if unit == "minutes":
        return task_duration // 60, "hours" + (task_duration % 60, "minutes")
    raise ValueError(f"Неизвестная единица: {unit}")
