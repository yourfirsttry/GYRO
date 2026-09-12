# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: VolunteerHub
class ChangeLog:
    def __init__(self):
        self._log = []

    def record(self, entity_type, entity_id, action, detail):
        self._log.append({
            'entity_type': entity_type,
            'entity_id': entity_id,
            'action': action,
            'detail': detail,
            'timestamp': datetime.now().isoformat(),
        })

    def get_log(self, entity_type=None, entity_id=None):
        if entity_type is None and entity_id is None:
            return self._log[:]
        if entity_type is not None:
            self._log = [e for e in self._log if e['entity_type'] == entity_type]
        if entity_id is not None:
            self._log = [e for e in self._log if e['entity_id'] == entity_id]
        return self._log[:]
