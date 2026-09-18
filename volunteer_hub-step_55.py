# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: VolunteerHub
def soft_check_duplicates(record_id, records):
    """Мягкая проверка: если id совпадает — предупредить, но не блокировать."""
    if record_id in records:
        print(f"⚠️  Дубликат записи с id={record_id} уже существует в базе.")
