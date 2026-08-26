# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: VolunteerHub
import unittest
from volunteerhub_app import VolunteerHub

class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        self.hub = VolunteerHub()

    def test_duplicate_volunteer_registration(self):
        self.hub.add_volunteer("Alice", "alice@example.com")
        self.hub.add_volunteer("Alice", "alice@example.com")
        self.assertEqual(len(self.hub.volunteers), 1)

    def test_invalid_date_format(self):
        self.hub.add_volunteer("Bob", "bob@example.com")
        with self.assertRaises(ValueError):
            self.hub.add_shift("Bob", "2023-13-01", "morning")

    def test_add_event_with_zero_volunteers(self):
        self.hub.add_volunteer("Charlie", "charlie@example.com")
        self.hub.add_shift("Charlie", "2023-12-01", "morning")
        event = self.hub.add_event("Morning Shift", "morning", ["Charlie"], 1)
        self.assertEqual(event['volunteers'], ["Charlie"])

    def test_event_without_volunteers(self):
        event = self.hub.add_event("Solo Event", "morning", [], 1)
        self.assertEqual(event['volunteers'], [])

    def test_add_report_with_no_volunteers(self):
        self.hub.add_volunteer("Diana", "diana@example.com")
        self.hub.add_shift("Diana", "2023-12-01", "morning")
        event = self.hub.add_event("Small Event", "morning", ["Diana"], 1)
        report = self.hub.add_report(event, 5, "Good job")
        self.assertEqual(report['volunteers_count'], 1)
        self.assertEqual(report['rating'], 5)
        self.assertEqual(report['comment'], "Good job")

if __name__ == "__main__":
    unittest.main()
