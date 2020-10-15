import unittest
from unittest.mock import Mock
from unittest.mock import patch
import Calendar
# Add other imports here if needed


class CalendarTest(unittest.TestCase):
    # This test tests number of upcoming events.
    def test_get_events_with_input(self):
        time = "2020-08-03T00:00:00.000000Z"

        mock_api = Mock()
        num_events = Calendar.get_events_with_input(mock_api)

        self.assertEqual(num_events, 0)

    # Add more test cases here


def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(CalendarTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)


main()
