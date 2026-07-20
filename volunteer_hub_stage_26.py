# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: VolunteerHub
def demo():
    print("=== VolunteerHub Demo ===")
    for v in volunteers:
        if v.status == 'active':
            shifts = ', '.join(s.start_time for s in v.shifts)
            print(f"  {v.name} ({v.role}) - shift: {shifts}")
    print("\nEvents:")
    for ev in events:
        attendees = [volunteers[i].name for i in range(len(volunteers)) if volunteers[i].id == ev.attendee_id]
        print(f"  {ev.name} ({len(attendees)} attended)")

demo()
