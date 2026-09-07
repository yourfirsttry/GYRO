# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: VolunteerHub
def demo():
    print("=== VolunteerHub Demo ===")
    hub = VolunteerHub()
    hub.add_event("День волонтёра", 2024, 6, 14, 9, 17, "площадь")
    hub.add_event("Марафон", 2024, 7, 1, 8, 20, "парк")
    hub.add_event("Концерт", 2024, 8, 10, 14, 22, "театр")
    hub.add_event("Фестиваль", 2024, 9, 5, 10, 23, "площадь")
    print(f"Событий: {hub.events_count}")
    print(f"События: {hub.list_events()}")
    print(f"События по дате: {hub.list_events_by_date()}")
    print(f"События по городу: {hub.list_events_by_city()}")
    print(f"События по городу-событие: {hub.list_events_by_city_event()}")
    print("=== Конец демо ===")
