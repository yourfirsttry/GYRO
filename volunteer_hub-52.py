# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: VolunteerHub
def export_short_report(events, volunteers, shifts, reports):
    """Export a concise text report of volunteer activities."""
    lines = []
    lines.append("=== VolunteerHub Short Report ===")
    lines.append(f"Total events: {len(events)}")
    lines.append(f"Total volunteers: {len(volunteers)}")
    lines.append(f"Total shifts: {len(shifts)}")
    lines.append(f"Total reports: {len(reports)}")
    lines.append("")
    for event in sorted(events, key=lambda e: e.get("start", "")):
        name = event.get("name", "Unknown")
        start = event.get("start", "N/A")
        end = event.get("end", "N/A")
        count = sum(1 for s in shifts if s.get("event_id") == id(event))
        lines.append(f"Event: {name} | {start} - {end} | Shifts: {count}")
    lines.append("")
    for vol in sorted(volunteers, key=lambda v: v.get("name", "")):
        name = vol.get("name", "Unknown")
        shifts_count = sum(1 for s in shifts if s.get("volunteer_id") == id(vol))
        lines.append(f"Volunteer: {name} | Shifts: {shifts_count}")
    lines.append("")
    if reports:
        lines.append("Recent Reports:")
        for r in sorted(reports, key=lambda r: r.get("date", ""), reverse=True)[:10]:
            lines.append(f"- Date: {r.get('date', 'N/A')} | Summary: {r.get('summary', 'N/A')}")
    else:
        lines.append("No reports yet.")
    return "\n".join(lines)
