# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: VolunteerHub
def calculate_monthly_stats(events, participants):
    from collections import defaultdict
    stats = defaultdict(lambda: {'total_hours': 0, 'participants_count': set()})
    for event in events:
        if not isinstance(event.get('date'), str) or len(event['date']) != 10: continue
        year_month = f"{event['date'][:4]}-{event['date'][5:7]}"
        hours = float(event.get('hours', 0))
        stats[year_month]['total_hours'] += hours
        for pid in event.get('participants', []):
            if isinstance(pid, int) and pid not in stats[year_month]['participants_count']:
                stats[year_month]['participants_count'].add(pid)
    return {k: {'hours': v['total_hours'], 'unique_participants': len(v['participants_count'])} for k, v in sorted(stats.items())}
