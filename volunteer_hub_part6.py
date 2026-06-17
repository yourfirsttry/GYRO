# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: VolunteerHub
def filter_records(records, filters=None):
    if not filters: return records
    for key, value in filters.items():
        if isinstance(value, list):
            records = [r for r in records if any(r.get(key) == v for v in value)]
        else:
            records = [r for r in records if r.get(key) == value]
    return records

def get_filtered_events(events=None, status='active', categories=None, tags=None):
    filters = {'status': status}
    if categories: filters['categories'] = categories
    if tags: filters['tags'] = tags
    return filter_records(events or [], filters)
