# === Stage 17: Добавь группировку записей по категориям ===
# Project: VolunteerHub
from collections import defaultdict, Counter
def group_by_category(records: list[dict], key_field: str) -> dict[str, list]:
    groups = defaultdict(list)
    for record in records:
        cat = record.get(key_field, 'Uncategorized')
        groups[cat].append(record)
    return {k: sorted(v, key=lambda x: x.get('date', '')) for k, v in groups.items()}

def get_category_stats(records: list[dict], key_field: str) -> dict[str, dict]:
    grouped = group_by_category(records, key_field)
    stats = {}
    for cat, items in grouped.items():
        counts = Counter(item.get('status', 'unknown') for item in items)
        total_hours = sum(item.get('hours', 0) for item in items)
        stats[cat] = {'count': len(items), 'total_hours': total_hours, 'statuses': dict(counts)}
    return stats
