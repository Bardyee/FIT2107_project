import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock
import Calendar
# Add other imports here if needed


class CalendarTest(unittest.TestCase):
    # This test tests number of upcoming events.
    def test_get_upcoming_events_number(self):
        num_events = 2
        time = "2020-08-03T00:00:00.000000Z"

        mock_api = Mock()
        events = Calendar.get_upcoming_events(mock_api, time, num_events)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        self.assertEqual(kwargs['maxResults'], num_events)

    # This test tests invalid number of upcoming events.
    def test_get_upcoming_events_number_error(self):
        num_events = 0
        time = "2020-08-03T00:00:00.000000Z"

        mock_api = Mock()

        with self.assertRaises(ValueError):
            events = Calendar.get_upcoming_events(mock_api, time, num_events)

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

class GetEventsWithInputTest(unittest.TestCase):
    # This test tests if year is empty.
    def test_get_events_with_input_empty(self):
        mock_api = Mock()
        with self.assertRaises(ValueError):
            events = Calendar.get_events_with_input(mock_api, "")

    # This test tests if only year is present.
    def test_get_events_with_input_only_year(self):

        year = "2020"

        mock_api = Mock()
        events = Calendar.get_events_with_input(mock_api, year)

        self.assertEqual(
            mock_api.events.return_value.list.return_value.execute.return_value.get.call_count, 1)

        args, kwargs = mock_api.events.return_value.list.call_args_list[0]
        self.assertEqual(kwargs['timeMin'], "2020-01-01T00:00:00Z")
        self.assertEqual(kwargs['timeMax'], "2020-12-31T23:59:59Z")

    # This test tests if year and month with 31 days are present.
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

    # This test tests if year and month with 30 days are present.
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

    # This test tests if leap year and month Febuary are present.
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

    # This test tests if non-leap year and month Febuary are present.
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

    # This test tests if year and month and day are all present.
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

class GetDetailsOfEventTest(unittest.TestCase):
    # This test tests getting details of event
    def test_get_details_of_event(self):
        mock_event = MagicMock()

        events = Calendar.get_details_of_event(mock_event)

        self.assertEqual(
            mock_event.events.return_value.list.return_value.execute.return_value.get.call_count, 0)
        self.assertEqual(events, mock_event)

class DeleteEventTest(unittest.TestCase):
    # This test tests deleting an event.
    def test_delete_event(self):
        mock_api = MagicMock()
        mock_events = MagicMock()

        event_deleted = Calendar.delete_event(mock_api, mock_events)

        self.assertTrue(event_deleted)

class GetEventWithKeywordTest(unittest.TestCase):
    # This test tests searching for an event with keyword.
    def test_get_event_with_keyword(self):
        mock_api = Mock()
        mock_api.events.return_value.list.return_value.execute.return_value = {
            "items": [
                {
                    "summary": "testSearch",
                    "id": "12345"
                },
                {
                    "summary": "testDontSeeThis",
                    "id": "24680"
                }
            ]
        }

        found_events = Calendar.get_events_with_keyword(mock_api, "Search")

        self.assertIn("testSearch", found_events[0]["summary"])
        self.assertNotIn("testDontSeeThis", found_events[0]["summary"])

    # This test tests searching for an event with invalid keyword.
    def test_get_event_with_invalid_keyword(self):
        mock_api = Mock()
        mock_api.events.return_value.list.return_value.execute.return_value = {
            "items": [
                {
                    "summary": "testSearch",
                    "id": "12345"
                }
            ]
        }

        with self.assertRaises(KeyError):
            found_events = Calendar.get_events_with_keyword(mock_api, "")

        found_events = Calendar.get_events_with_keyword(mock_api, "noEvent")

        self.assertEqual(found_events, None)

def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(CalendarTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(GetAllEventsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(GetEventsWithInputTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(GetDetailsOfEventTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(DeleteEventTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(GetEventWithKeywordTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


main()
