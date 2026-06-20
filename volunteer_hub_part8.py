# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: VolunteerHub
def run_menu():
    while True:
        print("\n=== VolunteerHub Меню ===")
        print("1. Список участников")
        print("2. Добавить участника")
        print("3. Управление сменами")
        print("4. Отчёты по событиям")
        print("5. Выход")
        choice = input("Выберите действие (1-5): ")
        if choice == "1":
            for u in participants:
                print(f"  {u['name']} ({u['role']})")
        elif choice == "2":
            name = input("Имя участника: ")
            role = input("Роль (volunteer/organizer): ")
            if not name or not role:
                print("Ошибка: заполните все поля.")
                continue
            participants.append({"name": name, "role": role})
            print(f"Участник {name} добавлен.")
        elif choice == "3":
            shift_id = input("ID смены (или 'new' для новой): ")
            if shift_id.lower() == "new":
                title = input("Название смены: ")
                date = input("Дата (YYYY-MM-DD): ")
                shifts.append({"id": len(shifts)+1, "title": title, "date": date})
                print(f"Смена '{title}' создана.")
            else:
                if shift_id.isdigit():
                    sid = int(shift_id) - 1
                    if 0 <= sid < len(shifts):
                        shifts[sid]["status"] = input("Статус (planned/active/completed): ")
                        print(f"Смена {sid+1} обновлена.")
        elif choice == "4":
            event_id = input("ID события: ")
            if event_id.isdigit():
                eid = int(event_id) - 1
                if 0 <= eid < len(events):
                    reports = events[eid].get("reports", [])
                    for r in reports:
                        print(f"Отчёт от {r['date']}: {r['summary']}")
        elif choice == "5":
            print("Выход из системы.")
            break
