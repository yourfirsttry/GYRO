# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: VolunteerHub
def calculate_weekly_stats(events, reports):
    from datetime import date, timedelta
    
    if not events:
        return []
    
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(weeks=1)
    
    weekly_data = {
        'week_start': week_start.isoformat(),
        'week_end': week_end.isoformat(),
        'total_hours': 0,
        'participants_count': set(),
        'events_count': 0,
        'reports_submitted': 0
    }
    
    for event in events:
        if week_start <= event['date'] < week_end:
            weekly_data['events_count'] += 1
            weekly_data['total_hours'] += event.get('duration', 0)
            weekly_data['participants_count'].update(event.get('volunteers', []))
    
    for report in reports:
        if week_start <= report['date'] < week_end and report.get('status') == 'submitted':
            weekly_data['reports_submitted'] += 1
    
    return [weekly_data]
