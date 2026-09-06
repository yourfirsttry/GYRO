# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: VolunteerHub
DATA_VERSION = 46
MIGRATION_46 = {
    "description": "Added event_type field to events and report_date to reports",
    "applies_to": ["events", "reports"],
    "fields": {
        "events": {"new": "event_type", "default": "general"},
        "reports": {"new": "report_date", "default": "2024-01-01"},
    },
}

def apply_migration_46(data):
    for record in data.get("events", []):
        if "event_type" not in record:
            record["event_type"] = "general"
    for record in data.get("reports", []):
        if "report_date" not in record:
            record["report_date"] = "2024-01-01"
    data["version"] = DATA_VERSION
    return data
