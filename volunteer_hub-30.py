# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: VolunteerHub
class Profile:
    def __init__(self, name, email=None, role='volunteer'):
        self.name = name
        self.email = email or ''
        self.role = role  # volunteer | admin | organizer
        self.tasks_completed = []
    
    def add_task(self, task):
        if task not in self.tasks_completed:
            self.tasks_completed.append(task)
    
    def summary(self):
        return f"{self.name} ({self.role}): {len(self.tasks_completed)} tasks"
