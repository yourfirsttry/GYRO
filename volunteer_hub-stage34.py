# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: VolunteerHub
class Template:
    def __init__(self, name, record_type):
        self.name = name
        self.record_type = record_type

    @property
    def fields(self):
        templates_db = {
            "shift": ["volunteer_id", "event_id", "start_time", "end_time"],
            "participant": ["first_name", "last_name", "email", "phone"],
            "event": ["name", "date", "location", "description"]
        }
        return templates_db.get(self.record_type, [])

    def create_record(self):
        record = {}
        for field in self.fields:
            record[field] = input(f"Введите значение для {field}: ")
        return record
