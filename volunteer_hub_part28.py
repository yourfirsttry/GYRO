# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: VolunteerHub
def summary_metrics():
    total_volunteers = len(volunteers)
    active_events = sum(1 for e in events if e.status == "active")
    hours_worked = 0
    for shift in shifts:
        hours_worked += shift.hours
    reports_count = len(reports)
    print(f"Volunteers: {total_volunteers}")
    print(f"Active events: {active_events}")
    print(f"Total hours worked: {hours_worked}")
    print(f"Reports submitted: {reports_count}")
