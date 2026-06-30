# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: VolunteerHub
def generate_summary():
    print("=== VolunteerHub Сводка ===")
    if participants:
        print(f"Участников: {len(participants)}")
        for p in participants[:3]:
            print(f"  - {p['name']}: статус={p.get('status', 'unknown')}")
    else:
        print("Участников нет.")

    if shifts:
        print(f"\nСмен запланировано: {len(shifts)}")
        for s in shifts[:3]:
            print(f"  - {s['event']} ({s.get('date', 'дата не указана')})")
    else:
        print("\nСмены отсутствуют.")

    if events:
        print(f"\nСобытий в базе: {len(events)}")
        for e in events[:3]:
            print(f"  - {e['name']}: мест={e.get('capacity', 'N/A')}, занято={e.get('registered', 0)}")
    else:
        print("\nСобытий нет.")

    if reports:
        print(f"\nОтчётов подано: {len(reports)}")
        for r in reports[:3]:
            print(f"  - {r['event']} ({r.get('date', 'дата не указана')})")
    else:
        print("\nОтчёты отсутствуют.")

    if participants and shifts and events and reports:
        total_hours = sum(r.get('hours', 0) for r in reports)
        print(f"\nВсего отработано часов (по отчётам): {total_hours}")
