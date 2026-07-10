# === Stage 20: Добавь восстановление записей из архива ===
# Project: VolunteerHub
def load_from_archive(archive_path, records):
    """Восстановление записей из архива: читает JSON с запоздалыми данными."""
    if not os.path.exists(archive_path):
        print("Архив не найден.")
        return 0
    with open(archive_path, 'r', encoding='utf-8') as f:
        archived = json.load(f)
    loaded = 0
    for item in archived:
        key_map = {
            "volunteer": Volunteer,
            "shift": Shift,
            "event": Event,
            "report": Report
        }
        cls = key_map.get(item.get("type", ""))
        if cls and not isinstance(cls, type):
            continue
        try:
            rec = cls.from_dict(item)
            records.append(rec)
            loaded += 1
        except Exception as e:
            print(f"Ошибка загрузки записи [{item.get('id', '?')}]: {e}")
    return loaded

def save_to_archive(records, archive_path):
    """Сохранение текущих записей в архив для последующего восстановления."""
    archived = []
    for rec in records:
        if hasattr(rec, 'to_dict'):
            archived.append(rec.to_dict())
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump(archived, f, ensure_ascii=False, indent=2)
    print(f"Архив сохранён в {archive_path} ({len(archived)} записей).")
