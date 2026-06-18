# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: VolunteerHub
def sort_records(records, key='date', reverse=False):
    if not records: return []
    order_map = {'high': 0, 'medium': 1, 'low': 2}
    date_key = lambda r: (r.get('date') or '').isoformat() if isinstance(r.get('date'), datetime) else str(r.get('date', ''))
    name_key = lambda r: str(r.get('name', '')).lower()
    priority_key = lambda r: order_map.get(str(r.get('priority', 'medium')).lower(), 1)
    
    sort_keys = {
        'date': (lambda x: date_key(x), reverse, False),
        'priority': (lambda x: priority_key(x), True, False),
        'name': (lambda x: name_key(x), False, True)
    }
    
    if key not in sort_keys: raise ValueError(f"Invalid sort key: {key}. Use 'date', 'priority' or 'name'.")
    sorter, asc, reverse = sort_keys[key]
    
    return sorted(records, key=sorter, reverse=(not asc) ^ (reverse is True))
