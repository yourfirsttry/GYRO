# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: VolunteerHub
def edit_record(record_id, updates):
    if record_id not in records:
        raise ValueError(f"Record {record_id} not found")
    
    for key, value in updates.items():
        if hasattr(records[record_id], key) and key != 'id':
            setattr(records[record_id], key, value)
        elif isinstance(getattr(records[record_id], key), list):
            records[record_id].key = [v for v in getattr(records[record_id], key) if not (isinstance(v, dict) and v.get('id') == record_id)] + [value]
    
    return records[record_id]
