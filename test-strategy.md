# **Test Strategy for FIT2107 Assignment 2**

## White Box testing methods used
We used path coverage, branch coverage as well as condition coverage to design test cases for our functions. Line coverage was not used as there are plenty of lines of code written to display a neat and simple UI, hence the functionality of those lines of code only extend to them displaying the right words.

`coverage run Calendar.py`\
This line was used to help ensure that we had sufficient test suites designed such that a high coverage of the functionality was achieved.

## Basic functionalities to cover:
1. Events from 5 years ago up to 2 years from now can be viewed.
2. The user can navigate through the dates in the calendar to filter the events from a single year, month, or date.
3. The user can search for events using key words.
4. The user can delete any events using key words.

### Test suite 1:
Description: To test that the user can get the upcoming events desired. \
Test cases: 

`0` - Gets 0 upcoming events.\
Expected output: Console prints "Invalid input"\
Real output: "Invalid input" printed\
Result: Pass

`2` - Gets 2 upcoming events.\
Expected output: 2 events\
Real output: 2 events\
Result: Pass

In the CalendarTest file, we assert that the timeMin must be the current time.

<br><br>
### Test suite 2:
Description: To test that the user can get all events from at least 5 years ago and at most 2 years later. \
Test cases: \
No inputs are required.

In the CalendarTest file, we assert that the timeMin is 5 years ago and timeMax is 2 years later.

<br><br>
### Test suite 3:
Description: To test that the user can get events based on date given. \
Test cases: 

#### All inputs tested for year: 
`2020` - A leap year\
`2022` - A non leap year\
`    ` - Empty string

#### All inputs tested for month:
`2` - Febuary which has 28/29 days\
`4` - A month with 30 days\
`5` - A month with 31 days\
`    ` - Empty string which will give a default value of starting time `01` and ending time `12`

#### All inputs tested for days:
`1` - All months will have 1
`    ` - Empty string which will give a default value of starting time `01` and ending time `28/29/30/31` depending on the month given

All combinations are properly picked and tested to ensure full branch coverage.\
The tested inputs combinations were:

### 1)
Year: ` `\
Month: `""`\
Day: `""`

### 2)
Year: `2020`\
Month: `04`\
Day: `""`

### 3)
Year: `2020`\
Month: `05`\
Day: `""`

### 4)
Year: `2020`\
Month: `04`\
Day: `""`

### 5)
Year: `2020`\
Month: `02`\
Day: `""`

### 6)
Year: `2021`\
Month: `02`\
Day: `""`

### 7)
Year: `2021`\
Month: `02`\
Day: `01`

Invalid inputs such as year = `str` or month = `53` or having days = `29` when year is not a leap year and month is febuary are handled in the main menu.

<br><br>
### Test suite 4:
Description: To test that the user can search for events using key words.\
Test cases: \
<!-- `    ` - Empty string to check if KeyError is raised.\
Expected output: Console prints "Invalid input"\
Real output: "Invalid input" printed\
Result: Pass -->

`Search` - Search for a premade event labelled "testSearch".\
Expected output: A list of events that contain the keyword "Search" is returned.\
Real output: A list with one result event ( testSearch )\
Result: Pass

`noEvent` - Search for an event that wasnt created.\
Expected output: Nothing is returned, and a message prints to the console stating that no events with given keyword is found.\
Real output: None was returned and "No events with the given keyword were found." is printed to the console.\
Result: Pass

Invalid keyword such as an empty string was handled in the main menu.

<br><br>
### Test suite 5:
Description: To test that the user can delete events from a list of events using index\
Test Cases:\

`mock_test` - Deleting an event with ID of "mock_test"\
Output should print a message showing the success of deletion\
Expected output: A success message printed to console and the method returns the deleted event object.
Real output: Success message was printed and method returned the deleted event object
Result: Pass

Invalid indices like an empty string or an index out of bounds was handled in the main menu.

<br><br>
### Test suite 6:
Description: To test the menu\
Test Cases:

`0` - Selecting a command that doesn't exist.\
Expected output: console prints "invalid command"\
Real output: "invalid command"

`a` - Using a letter.\
Expected output: console prints "invalid command"\
Real output: "invalid command"

` ` - Leaving input empty.\
Expected output: console prints "invalid command"\
Real output: "invalid command"

`2` - Selecting the get all events command\
Expected output: get_all_events() runs and all events are printed.\
Real output: get_all_events() runs and all events are printed. 