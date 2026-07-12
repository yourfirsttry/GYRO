# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: VolunteerHub
def add_reminder(tasks, name, task_date):
    reminder = {
        'name': name,
        'task_date': task_date,
        'status': 'pending'
    }
    tasks.append(reminder)
    return reminder


reminders = []
add_reminder(reminders, "John", 1725148800)
add_reminder(reminders, "Jane", 1725235200)

def get_upcoming_reminders(now):
    return [r for r in reminders if r['task_date'] > now and r['status'] == 'pending']


now = int(time.time())
upcoming = get_upcoming_reminders(now)
print(f"У вас {len(upcoming)} напоминания:")
for r in upcoming:
    print(r['name'], "—", datetime.fromtimestamp(r['task_date']).strftime('%Y-%m-%d'))
