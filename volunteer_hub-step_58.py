# === Stage 58: Добавь простую систему пользовательских представлений списка ===
# Project: VolunteerHub
def register_view(view_func):
    """Register a simple list view function. The view receives a list of items and returns a formatted string."""
    _views.append(view_func)

def get_view(items, view_name='default'):
    """Get a registered view function by name and apply it to items. Returns formatted string or default repr."""
    for view in _views:
        if view_name in view.__name__ or view_name == 'default':
            return view(items)
    return repr(items)

def list_participants():
    """List all participants with their IDs and names."""
    def view(participants):
        lines = ['ID\tName', '---\t---']
        for p in participants:
            lines.append(f'{p["id"]}\t{p["name"]}')
        return '\n'.join(lines)
    view.__name__ = 'list_participants'
    register_view(view)

def list_shifts():
    """List all shifts with their dates and durations."""
    def view(shifts):
        lines = ['Date\tDuration', '-----\t--------']
        for s in shifts:
            lines.append(f'{s["date"]}\t{s["duration"]}ч')
        return '\n'.join(lines)
    view.__name__ = 'list_shifts'
    register_view(view)

def list_events():
    """List all events with their names and locations."""
    def view(events):
        lines = ['Name\tLocation', '-----\t--------']
        for e in events:
            lines.append(f'{e["name"]}\t{e["location"]}')
        return '\n'.join(lines)
    view.__name__ = 'list_events'
    register_view(view)

def list_reports():
    """List all reports with their summaries."""
    def view(reports):
        lines = ['Summary', '--------']
        for r in reports:
            lines.append(r['summary'])
        return '\n'.join(lines)
    view.__name__ = 'list_reports'
    register_view(view)
