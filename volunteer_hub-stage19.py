# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: VolunteerHub
def archive_records(records, cutoff_days=30):
    """Archive completed or old records older than cutoff_days."""
    import datetime
    today = datetime.date.today()
    cutoff = today - datetime.timedelta(days=cutoff_days)
    archived = []
    for r in records:
        if (r.get("status") == "completed" and r.get("end_date")) or \
           r.get("created_at", "") < str(cutoff):
            r["archived"] = True
            r["archive_date"] = today.isoformat()
            archived.append(r)
    return archived
