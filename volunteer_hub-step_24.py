# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: VolunteerHub
def print_volunteer_record(volunteer):
    """Compact one-line view of a volunteer: name, role, hours, status."""
    status = "active" if not volunteer["status"] or volunteer["status"] == "completed" else volunteer["status"]
    return (f"{volunteer['name']:20s} | {str(volunteer.get('role', 'General'))[:15]:<15s} | "
            f"{int(volunteer.get('hours', 0)):>4d}h | status: {status}")
