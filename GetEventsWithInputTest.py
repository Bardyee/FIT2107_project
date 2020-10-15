import unittest
from unittest.mock import Mock
from unittest.mock import patch
import Calendar
# Add other imports here if needed


class CalendarTest(unittest.TestCase):
    # This test tests number of upcoming events.
    @patch('Calendar.input', return_value="q")
    def test_get_events_with_input(self):
        num_events = 1
        time = "2020-08-03T00:00:00.000000Z"

        
        mock_api = Mock()
        num_events = Calendar.get_events_with_input(mock_api)

        # self.assertEqual(
        #     mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        # args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        # self.assertEqual(kwargs['maxResults'], num_events)

    # Add more test cases here


def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(CalendarTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)


main()
