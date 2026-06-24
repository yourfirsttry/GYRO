# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: VolunteerHub
def export_to_json():
    import json
    state = {
        "participants": participants,
        "shifts": shifts,
        "events": events,
        "reports": reports,
        "metadata": {"version": 10, "timestamp": datetime.now().isoformat()}
    }
    return json.dumps(state, ensure_ascii=False, indent=2)
