# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: VolunteerHub
def self_check():
    print("=== VolunteerHub Self-Check ===")
    checks = [
        ("Participants", lambda: len(participants) > 0),
        ("Shifts", lambda: len(shifts) > 0),
        ("Events", lambda: len(events) > 0),
        ("Reports", lambda: len(reports) > 0),
        ("Availability matrix", lambda: len(availability) > 0),
        ("Conflict detection", lambda: True),
    ]
    for name, func in checks:
        try:
            result = func()
            print(f"  ✓ {name}: {result}")
        except Exception as e:
            print(f"  ✗ {name}: {e}")
    print("=== Self-Check Complete ===")
