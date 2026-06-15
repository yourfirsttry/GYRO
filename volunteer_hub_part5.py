# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: VolunteerHub
def delete_record(collection_name, record_id):
    if collection_name not in db:
        raise ValueError(f"Collection '{collection_name}' does not exist.")
    if record_id not in db[collection_name]:
        raise ValueError(f"No record with id {record_id} found in '{collection_name}'.")
    del db[collection_name][record_id]

def handle_missing_ids(collection_name, target_field):
    if collection_name not in db:
        return []
    missing = [rid for rid in db[collection_name].keys() if rid is None or rid == ""]
    if missing:
        print(f"Warning: Found {len(missing)} records with empty/missing '{target_field}' IDs in '{collection_name}'.")
    return missing

def cleanup_orphaned_reports():
    events = db.get("events", {})
    shifts = db.get("shifts", {})
    reports = db.get("reports", {})
    valid_event_ids = set(events.keys()) if events else set()
    valid_shift_ids = set(shifts.keys()) if shifts else set()
    orphaned = [rid for rid in reports.keys() if rid not in valid_event_ids and rid not in valid_shift_ids]
    if orphaned:
        print(f"Cleaning up {len(orphaned)} orphaned report records.")
        for rid in orphaned:
            del db["reports"][rid]
