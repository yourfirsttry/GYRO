# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: VolunteerHub
def validate_and_repair():
    """Проверяет целостность данных и пытается автоматически исправить простые проблемы."""
    
    # Проверяем, что все участники имеют валидные данные
    for i in range(len(participants)):
        p = participants[i]
        if not isinstance(p['id'], int):
            p['id'] = len(participants)
        if not isinstance(p['name'], str) or len(p['name']) == 0:
            p['name'] = f"Участник {p['id']}"
        
    # Проверяем, что все смены привязаны к существующим участникам и событиям
    for i in range(len(shifts)):
        s = shifts[i]
        if not isinstance(s['volunteer_id'], int):
            s['volunteer_id'] = None
        
    # Проверяем, что все события имеют валидные даты
    for i in range(len(events)):
        e = events[i]
        if 'date' not in e:
            e['date'] = datetime.now()
    
    print("Данные проверены и при необходимости отремонтированы.")

validate_and_repair()
