import unittest
from unittest.mock import Mock
import Calendar
# Add other imports here if needed


class GetAllEventsTest(unittest.TestCase):
    # This test tests if timeMin is set correctly.
    def test_get_all_events_timeMin(self):
        time = "2020-08-03T00:00:00.000000Z"

        mock_api = Mock()
        events = Calendar.get_all_events(mock_api, time)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]

        self.assertEqual(kwargs['timeMin'], "2015-08-03T00:00:00.000000Z")

    # This test tests if timeMax is set correctly
    def test_get_all_events_timeMax(self):
        time = "2020-08-03T00:00:00.000000Z"

        mock_api = Mock()
        events = Calendar.get_all_events(mock_api, time)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]

        self.assertEqual(kwargs['timeMax'], "2022-08-03T00:00:00.000000Z")



def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(GetAllEventsTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)


main()