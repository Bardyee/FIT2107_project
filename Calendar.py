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
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


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

    # self recording some methods
    # convert str to date
    # x = datetime.date.fromisoformat(str_of_current_date) where str_of_current_date in YYYY-MM-DD

def get_events_with_input(api):
    """
    Gets all events from date specified
    """
    validYear = False
    validMonth = False
    validDay = False
    year=""
    month=""
    day=""
    print("Leave empty if filter not needed")

    while not validYear:
        print("Input year in YYYY format")
        year = input("Filter year: ")
        if year=="":
            validYear=True
            continue
        try:
            int(year)
        except ValueError:
            print("Invalid year input, please try again")
            continue
        else:
            if int(year)<1 or int(year)>9999:
                print("Invalid year input, please try again")
                continue
            else:
                validYear=True

    while not validMonth:
        if year=="":
            break
        print("Input year in MM format")
        month = input("Filter month: ")
        if month=="":
            validMonth=True
            continue
        try:
            int(month)
        except ValueError:
            print("Invalid month input, please try again")
            continue
        else:
            if int(month)<1 or int(month)>12:
                print("Invalid month input, please try again")
                continue
            else:
                validMonth=True

    while not validDay:
        if month=="":
            break
        print("Input year in DD format")
        day = input("Filter day: ")
        if day=="":
            validDay=True
            continue
        try:
            int(day)
        except ValueError:
            print("Invalid day input, please try again")
            continue
        else:
            # if Feb
            if int(month) == 2:
                # if leap year:
                if int(year)% 4==0 and (int(year)%100!=0 or int(year)%400==0):
                    if int(day)<1 or int(day)>29:
                        print("Invalid day input, please try again")
                        continue
                # if not leap year
                else:
                    if int(day)<1 or int(day)>28:
                        print("Invalid day input, please try again")
                        continue

            # if Apr, Jun, Sep, Nov
            elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
                if int(day)<1 or int(day)>30:
                    print("Invalid day input, please try again")
                    continue

            # if Jan, Mar, May, Jul, Aug, Oct, Dec
            else:
                if int(day)<1 or int(day)>31:
                    print("Invalid day input, please try again")
                    continue
            
            validDay=True
    
    if year=="":
        print("No filters were used, returning to menu...\n")
        return None

    elif month=="":
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

    while events:
        list_of_events = []
        index=0
        for event in events:
            one_event = (index, (event['start'].get('dateTime', event['start'].get('date')), event['summary']))
            list_of_events.append(one_event)
            print(one_event)
            index+=1

        print("Please input an index to see more details of an event, else input q to leave this page")
        index_input = input()
        if index_input == "q":
            return None
        try:
            int(index_input)
        except ValueError:
            print("Invalid index")
        else:
            for t_event in list_of_events:
                if int(index_input) == t_event[0]:
                    event = events[int(index_input)]
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    print("\n")
                    print("event name: " + event['summary'])
                    print("created: " + event['created'])
                    print("creator: " + event['creator']['email'])
                    print("organizer: " + event['organizer']['email'])
                    print("start time: " + str(event['start']['dateTime']))
                    print("end time: " + str(event['end']['dateTime']))
                    print("reminders: " + str(event['reminders']))
                    print("\n")
    if not events:
        print('No upcoming events found.')
    return None

def get_events_with_keyword(api, keyword): 
    """
    Prints the start and details of a given event on the user's calendar.
    """
    print("\n")
    if(keyword == ""):
        raise KeyError("Keyword must contain 1 or more characters")

    events_results = api.events().list(calendarId='primary', singleEvents=True,
                                        orderBy='startTime').execute()
    
    event_list = events_results.get('items', [])
    index = 0
    for event in event_list:
        title = event['summary']
        if (keyword.lower() in title.lower()):
            index += 1
            print(title)
    if (index == 0):
        print("No events with the given keyword were found.")
    print("\n")
    return None

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
        # print("Reminders")
        # for event in events:
        #     print(event['reminders'])

    # def printing_reminders(reminders):
    #     print("\nReminders:")
    #     for reminder in reminders:
    #         print(reminder['reminder'])

    while running:
        print("Menu:")
        print("Select option by inputting the number assosiated with command")
        print("1: get upcoming events")
        print("2: get all events")
        print("3: get events with user input")
        print("4: get events with keyword")
        print("q: quit the program")
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
            get_events_with_input(api)

        elif u_input == "4":
            key = input("Search for...")
            if not key:
                print('\nInvalid input\n')
            else:
                get_events_with_keyword(api, key)

        elif u_input == "q":
            print("shutting down program...")
            running=False

        else:
            print("invalid command")


if __name__ == "__main__":  # Prevents the main() function from being called by the test suite runner
    main()
