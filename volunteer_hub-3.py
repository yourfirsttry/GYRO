# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: VolunteerHub
class VolunteerHub:
    def __init__(self):
        self.participants = {}
        self.shifts = []
        self.events = []
        self.reports = []

    def add_participant(self, name, email, phone):
        if not any(p['email'] == email for p in self.participants.values()):
            self.participants[email] = {'name': name, 'phone': phone}
            return True
        return False

    def create_shift(self, event_id, volunteer_email, start_time, end_time):
        shift = {
            'id': len(self.shifts) + 1,
            'event_id': event_id,
            'volunteer_email': volunteer_email,
            'start_time': start_time,
            'end_time': end_time
        }
        self.shifts.append(shift)
        return shift

    def create_event(self, title, description, date):
        event = {
            'id': len(self.events) + 1,
            'title': title,
            'description': description,
            'date': date
        }
        self.events.append(event)
        return event

    def submit_report(self, shift_id, notes, rating):
        report = {
            'shift_id': shift_id,
            'notes': notes,
            'rating': rating
        }
        self.reports.append(report)
        return report
