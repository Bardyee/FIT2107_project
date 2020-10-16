# Make sure you are logged into your Monash student account.
# Go to: https://developers.google.com/calendar/quickstart/python
# Click on "Enable the Google Calendar API"
# Configure your OAuth client - select "Desktop app", then proceed
# Click on "Download Client Configuration" to obtain a credential.json file
# Do not share your credential.json file with anybody else, and do not commit it to your A2 git repository.
# When app is run for the first time, you will need to sign in using your Monash student account.
# Allow the "View your calendars" permission request.


# Students must have their own api key
# No test cases needed for authentication, but authentication may required for running the app very first time.
# http://googleapis.github.io/google-api-python-client/docs/dyn/calendar_v3.html


# Code adapted from https://developers.google.com/calendar/quickstart/python
from __future__ import print_function
import datetime
import pickle
import os.path
import calendar
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def get_calendar_api():
    """
    Get an object which allows you to consume the Google Calendar API.
    You do not need to worry about what this function exactly does, nor create test cases for it.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)

def get_upcoming_events(api, starting_time, number_of_events):
    """
    Shows basic usage of the Google Calendar API.
    Prints the start and name of the next n events on the user's calendar.
    """
    if (number_of_events <= 0):
        raise ValueError("Number of events must be at least 1.")

    events_result = api.events().list(calendarId='primary', timeMin=starting_time,
                                      maxResults=number_of_events, singleEvents=True,
                                      orderBy='startTime').execute()
    return events_result.get('items', [])
    
    # Add your methods here.

def get_all_events(api, current_time):
    # line coverage
    """
    Gets all events from at least 5 years in the past and at least 2 years in the future
    """
    str_of_current_date = current_time[:10] # takes just YYYY-MM-DD
    future_year = str(int(current_time[:4]) + 2) # takes the current year and +2
    future_date = future_year + current_time[4:]
    past_year = str(int(current_time[:4]) - 5) # takes the current year and -5
    past_date = past_year + current_time[4:]
    events_result = api.events().list(calendarId='primary', timeMin=past_date,
                                  timeMax=future_date, singleEvents=True,
                                  orderBy='startTime').execute()
    return events_result.get('items', [])

def get_events_with_input(api, year, month="", day=""):
    """
    Gets all events from date specified
    """
    if year=="":
        raise ValueError

    if month=="":
        start_date = year + "-01-01"
        end_date = year + "-12-31"

    elif day=="":
        start_date = year + "-" + month + "-01"

        # if Feb
        if int(month) == 2:
            # if leap year:
            if int(year)% 4==0 and (int(year)%100!=0 or int(year)%400==0):
                end_date = year + "-" + month + "-29"
            # if not leap year
            else:
                end_date = year + "-" + month + "-28"

        # if Apr, Jun, Sep, Nov
        elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
            end_date = year + "-" + month + "-30"

        # if Jan, Mar, May, Jul, Aug, Oct, Dec
        else:
            end_date = year + "-" + month + "-31"

    else:
        start_date = year + "-" + month + "-" + day
        end_date = year + "-" + month + "-" + day

    start_of_date = start_date + "T00:00:00Z"
    end_of_date = end_date + "T23:59:59Z"
    events_result = api.events().list(calendarId='primary', timeMin=start_of_date,
                                  timeMax=end_of_date, singleEvents=True,
                                  orderBy='startTime').execute()

    events = events_result.get('items', [])

    return events

def get_details_of_event(event):
    """
    Gets the details of an event
    """
    
    print("\n")
    print("event name: " + event['summary'])
    print("created: " + event['created'])
    print("creator: " + event['creator']['email'])
    print("organizer: " + event['organizer']['email'])
    print("start time: " + str(event['start']['dateTime']))
    print("end time: " + str(event['end']['dateTime']))
    print("reminders: " + str(event['reminders']))
    print("\n")

def get_events_with_keyword(api, keyword): 
    """
    Prints the index and name of a given event from the user's calendar.
    """
    print("\n")
    if(keyword == ""):
        raise KeyError("Keyword must contain 1 or more characters")

    events_results = api.events().list(calendarId='primary', singleEvents=True,
                                        orderBy='startTime').execute()
    
    event_list = events_results.get('items', [])
    index = 0
    event_array = []
    for event in event_list:
        title = event['summary']
        eventID = event['id']
        if (keyword.lower() in title.lower()):
            event_array.append(event)
            index +=1
    if (index == 0):
        print("No events with the given keyword were found.\n")
        return None
    else:
        for x in range(len(event_array)):
            print(x, event_array[x]['summary'])
        print("\n")
        return (event_array)

def delete_event(api, event):
    """
    Deletes a given event.
    """
    api.events().delete(calendarId='primary', eventId=event['id']).execute()
    print("Event titled: "+event['summary']+" successfully deleted.")
    print("\n")
    return event

def main():
    api = get_calendar_api()
    time_now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    running = True

    def printing_events(events):
        print("\nEvents:")
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
        print("\n")

    while running:
        print("Menu:\nSelect option by inputting the number assosiated with command\n1: get upcoming events\n2: get all events\n3: get events with user input\n4: get events with keyword\n5: get all events with keyword and select one to delete\nq: quit the program\n")
        u_input = input("Input here: ")

        if u_input == "1":
            u_input_2 = input("How many events ahead do you want to see? ")
            try:
                events = get_upcoming_events(api, time_now, int(u_input_2))
            except ValueError:
                print('\nInvalid input\n')
            else:
                printing_events(events)

        elif u_input == "2":
            events = get_all_events(api, time_now)
            printing_events(events)

        elif u_input == "3":
            u_year = input("Input year in YYYY format: ")
            u_month = input("Input month in MM format: ")
            u_day = input("Input day in DD format: ")
            try:
                events = get_events_with_input(api, u_year, u_month, u_day)
            except:
                print("Invalid input")
            else:
                list_of_events = []
                index=0
                for event in events:
                    print(index, event['summary'])
                    index+=1
                index_input = input("Please input an index to see more details of an event: ")
                try:
                    get_details_of_event(events[int(index_input)])
                except:
                    print("invalid index")
                    

        elif u_input == "4":
            key = input("Search for... ")
            try:
                get_events_with_keyword(api, key)
            except KeyError:
                print('\nInvalid input\n')

        elif u_input == "5":
            key = input("Delete event titled... ")
            try:
                eventNum = get_events_with_keyword(api, key)
            except KeyError:
                print('\nInvalid input\n')

            if (eventNum is not None):
                index = input("Select an index to delete: ")
                try:
                    eventNum[int(index)]
                except:
                    print('\nInvalid index\n')
                else:
                    event = eventNum[int(index)]
                    delete_event(api, event)

        elif u_input == "q":
            print("shutting down program...")
            running=False

        else:
            print("invalid command")

if __name__ == "__main__":  # Prevents the main() function from being called by the test suite runner
    main()