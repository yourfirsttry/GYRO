# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: VolunteerHub
def undo_last_action(actions_log):
    """Undo the last action from the actions log if available."""
    if not actions_log or len(actions_log) == 0:
        print("No actions to undo.")
        return None
    
    last_action = actions_log.pop()
    
    # Revert based on action type
    action_type = last_action.get("type")
    data = last_action.get("data")
    
    if action_type == "register_volunteer":
        VolunteerHub.volunteers.remove(data["volunteer"])
    elif action_type == "create_shift":
        VolunteerHub.shifts.remove(data["shift"])
    elif action_type == "add_event":
        VolunteerHub.events.pop()  # Remove last event
    elif action_type == "generate_report":
        print("Report generation is not reversible.")
        return None
    
    print(f"Action undone: {action_type}")
    return data

# Example usage
# actions_log = [
#     {"type": "register_volunteer", "data": {"volunteer": VolunteerHub.volunteers[0]}},
#     {"type": "create_shift", "data": {"shift": VolunteerHub.shifts[0]}}
# ]
# undo_last_action(actions_log)
