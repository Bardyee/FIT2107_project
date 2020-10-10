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
    date = ""
    valid_date=False

    while not valid_date:
        date = input("Input date in YYYY-MM-DD format: ")

        # checks if format is XXXX-XX-XX
        if len(date)!=10 or date[4]!="-" or date[7]!="-":
            print("Invalid date, please try again")
            print(len(date))
            print(date[5])
            print(date[8])
            continue
        
        # checks if valid year
        try:
            int(date[:4])
        except ValueError:
            print("Invalid year input, please try again")
            continue
        else:
            if int(date[:4])<0 or int(date[:4])>9999:
                print("Invalid year input, please try again")
                continue
        
        # checks if valid month
        try:
            int(date[5:7])
        except ValueError:
            print("Invalid month input, please try again")
            continue
        else:
            if int(date[5:7])<0 or int(date[5:7])>12:
                print("Invalid month input, please try again")
                continue
        
        # checks if valid day
        try:
            int(date[8:10])
        except ValueError:
            print("Invalid day input, please try again")
            continue
        else:
            # if Feb
            if int(date[5:7]) == 2:
                # if leap year:
                if int(date[:4])% 4==0 and (int(date[:4])%100!=0 or int(date[:4])%400==0):
                    if int(date[8:10])<0 or int(date[8:10])>29:
                        print("Invalid day input, please try again")
                        continue
                # if not leap year
                else:
                    if int(date[8:10])<0 or int(date[8:10])>28:
                        print("Invalid day input, please try again")
                        continue

            # if Apr, Jun, Sep, Nov
            elif int(date[5:7]) == 4 or int(date[5:7]) == 6 or int(date[5:7]) == 9 or int(date[5:7]) == 11:
                if int(date[8:10])<0 or int(date[8:10])>30:
                    print("Invalid day input, please try again")
                    continue

            # if Jan, Mar, May, Jul, Aug, Oct, Dec
            else:
                if int(date[8:10])<0 or int(date[8:10])>31:
                    print("Invalid day input, please try again")
                    continue

        valid_date=True

    start_of_date = date + "T00:00:00Z"
    end_of_date = date + "T23:59:59Z"
    events_result = api.events().list(calendarId='primary', timeMin=start_of_date,
                                  timeMax=end_of_date, singleEvents=True,
                                  orderBy='startTime').execute()
    return events_result.get('items', [])

def main():
    api = get_calendar_api()
    time_now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    # events = get_upcoming_events(api, time_now, 10)
    # events = get_all_events(api, time_now)
    events = get_events_with_input(api)

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


if __name__ == "__main__":  # Prevents the main() function from being called by the test suite runner
    main()
