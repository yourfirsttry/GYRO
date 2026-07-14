# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: VolunteerHub
def check_overdue_reminders():
    """Проверка просроченных напоминаний для смен в будущем."""
    today = datetime.now().date()
    overdue = []
    for shift in shifts:
        if shift["end_date"] > today and "reminder_sent" not in shift:
            remaining = (shift["end_date"] - today).days
            if remaining <= 3:
                reminder = {
                    "message": f"Смена {shift['id']} заканчивается через {remaining} дней",
                    "action": "notify_volunteers",
                    "target_id": shift["volunteer_ids"],
                    "priority": "high" if remaining == 1 else "medium"
                }
                overdue.append(reminder)
    return overdue
