# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: VolunteerHub
def get_next_action(volunteer, shifts_history):
    """Recommend next action for a volunteer based on their history."""
    if not shifts_history:
        return "Join your first shift"
    
    last_shift = max(shifts_history.keys())
    total_hours = sum(shifts_history.values())
    
    if total_hours < 20:
        return f"Complete more shifts to reach 20 hours (currently {total_hours}h)"
    elif "report" not in shifts_history[last_shift]:
        return "Submit shift report for your last completed shift"
    else:
        next_available = min(s for s in shifts_history if s > last_shift)
        if next_available is None:
            return "Check back later for new shifts"
        else:
            return f"Next available shift starts at {next_available} UTC"
