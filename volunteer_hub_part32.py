# === Stage 32: Добавь журнал действий пользователя ===
# Project: VolunteerHub
class ActionLog:
    def __init__(self):
        self._entries = []

    def log(self, user_id, action_type, description):
        entry = {
            "id": len(self._entries) + 1,
            "user_id": user_id,
            "action_type": action_type,
            "description": description,
            "timestamp": datetime.now().isoformat(),
        }
        self._entries.append(entry)

    def get_entries(self):
        return list(reversed(self._entries))

    def clear(self):
        self._entries.clear()


volunteer_hub.action_log = ActionLog()
