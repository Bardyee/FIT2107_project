import unittest
from unittest.mock import Mock
import Calendar
# Add other imports here if needed


class GetEventsWithInputTest(unittest.TestCase):
    # This test tests number of upcoming events.
    def test_get_events_with_input_empty(self):
        mock_api = Mock()
        with self.assertRaises(ValueError):
            events = Calendar.get_events_with_input(mock_api, "")

    def test_get_events_with_input_only_year(self):
        year = "2020"

        mock_api = Mock()
        events = Calendar.get_events_with_input(mock_api, year)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        self.assertEqual(kwargs['timeMin'], "2020-01-01T00:00:00Z")
        self.assertEqual(kwargs['timeMax'], "2020-12-31T23:59:59Z")


    def test_get_events_with_input_year_and_big_month(self):
        year = "2020"
        month = "05"

        mock_api = Mock()
        events = Calendar.get_events_with_input(mock_api, year, month)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        self.assertEqual(kwargs['timeMin'], "2020-05-01T00:00:00Z")
        self.assertEqual(kwargs['timeMax'], "2020-05-31T23:59:59Z")

    def test_get_events_with_input_year_and_small_month(self):
        year = "2020"
        month = "04"

        mock_api = Mock()
        events = Calendar.get_events_with_input(mock_api, year, month)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        self.assertEqual(kwargs['timeMin'], "2020-04-01T00:00:00Z")
        self.assertEqual(kwargs['timeMax'], "2020-04-30T23:59:59Z")

    def test_get_events_with_input_leapyear_and_febuary(self):
        year = "2020"
        month = "02"

        mock_api = Mock()
        events = Calendar.get_events_with_input(mock_api, year, month)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        self.assertEqual(kwargs['timeMin'], "2020-02-01T00:00:00Z")
        self.assertEqual(kwargs['timeMax'], "2020-02-29T23:59:59Z")

    def test_get_events_with_input_nonleapyear_and_febuary(self):
        year = "2021"
        month = "02"

        mock_api = Mock()
        events = Calendar.get_events_with_input(mock_api, year, month)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        self.assertEqual(kwargs['timeMin'], "2021-02-01T00:00:00Z")
        self.assertEqual(kwargs['timeMax'], "2021-02-28T23:59:59Z")

    def test_get_events_with_input_year_and_small_month_and_day(self):
        year = "2021"
        month = "04"
        day = "01"

        mock_api = Mock()
        events = Calendar.get_events_with_input(mock_api, year, month, day)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        self.assertEqual(kwargs['timeMin'], "2021-04-01T00:00:00Z")
        self.assertEqual(kwargs['timeMax'], "2021-04-01T23:59:59Z")


    # Add more test cases here


def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(GetEventsWithInputTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)


main()

# try get_detail_of_event(mock_event)