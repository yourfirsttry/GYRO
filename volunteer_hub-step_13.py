# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: VolunteerHub
def multi_field_search(query, data_list, fields=None):
    if not query: return []
    if fields is None: fields = ['name', 'role', 'event_name']
    q_lower = query.lower()
    results = [item for item in data_list if any(q_lower in str(getattr(item, f, '')).lower() for f in fields)]
    return results
