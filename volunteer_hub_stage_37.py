# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: VolunteerHub
import unittest

class TestVolunteerHub(unittest.TestCase):
    def test_event_creation(self):
        event = Event("Test Event", "2024-01-15", 10)
        self.assertEqual(event.name, "Test Event")
        self.assertEqual(event.date, "2024-01-15")
        self.assertEqual(event.capacity, 10)

    def test_participant_creation(self):
        participant = Participant("John Doe", "john@example.com")
        self.assertEqual(participant.name, "John Doe")
        self.assertEqual(participant.email, "john@example.com")

    def test_shift_assignment(self):
        shift = Shift("Morning", "2024-01-15", 8)
        volunteer = Volunteer("Jane Smith")
        shift.assign_volunteer(volunteer)
        self.assertIn(volunteer, shift.volunteers)

    def test_task_creation(self):
        task = Task("Setup", "2024-01-15", 2, "Morning")
        self.assertEqual(task.name, "Setup")
        self.assertEqual(task.date, "2024-01-15")
        self.assertEqual(task.duration, 2)

    def test_report_generation(self):
        report = Report("Weekly", "2024-01-20")
        self.assertEqual(report.title, "Weekly")
        self.assertEqual(report.date, "2024-01-20")

if __name__ == '__main__':
    unittest.main()
