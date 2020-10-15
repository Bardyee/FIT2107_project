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

`1` - Gets 1 upcoming event, which at this time is "PASS S2, 2020- FIT2102 (Slot 4)".\
Expected output: Console shows "PASS S2, 2020- FIT2102 (Slot 4)" event\
Real output: "2020-10-22T12:00:00+08:00 PASS S2, 2020- FIT2102 (Slot 4)" printed\
Result: Pass

<br><br>
### Test suite 2:
Description: To test that the user can get all events from at least 5 years ago and at most 2 years later. \
Test cases: \
No inputs are required.

<br><br>
### Test suite 3:
Description: To test that the user can get events based on date given. \
Test cases: 

#### All inputs tested for year: 
`0` - Year 0 is invalid\
`10000` - Year 10000 is invalid\
`a` - Input cannot be letters\
`2020` - A leap year\
`2022` - A non leap year\
`    ` - Empty string

#### All inputs tested for month:
`0` - Month 0 is invalid\
`13` - Month 13 is invalid\
`a` - Input cannot be letters\
`2` - Febuary which has 28/29 days\
`4` - A month with 30 days\
`5` - A month with 31 days\
`    ` - Empty string

#### All inputs tested for days:
`0` - Day 0 is invalid\
`a` - Input cannot be letters\
`29` - If month is Febuary and on a non leap year, it is invalid\
`30` - If month is Febuary, it is invalid\
`31` - If month is Febuary, April, June, September, November, it is invalid\
`32` - It is invalid\
`    ` - Empty string

#### All inputs tested for index:
`0` - Prints the details of the event with index 0\
`q` - Exits the index selection menu\
`a` - Invalid index\
` ` - Empty string is an invalid index\
`9999` - If index is out of bounds, console will print "invalid index"

All combinations are properly picked and tested to ensure full branch coverage.\
The tested inputs combinations were:

### 1)
Year: `0`\
Year: `10000`\
Year: `a`\
Year: `""`

### 2)
Year: `2022`\
Month: `0`\
Month: `13`\
Month: `a`\
Month: `""`\
Index: `999`

### 3)
Year: `2022`\
Month: `2`\
Day: `a`\
Day: `0`\
Day: `29`\
Day: `28`

### 4)
Year: `2022`\
Month: `2`\
Day: `""`

### 5)
Year: `2022`\
Month: `4`\
Day: `0`\
Day: `31`\
Day: `""`

### 6)
Year: `2022`\
Month: `5`\
Day: `0`\
Day: `32`\
Day: `""`\
Index: `0`\
Index: `q`

### 7)
Year: `2020`\
Month: `2`\
Day: `""`\
Index: `""`

### 7)
Year: `2020`\
Month: `2`\
Day: `0`\
Day: `30`\
Day: `29`\
Index: `a`


<br><br>
### Test suite 4:
Description: To test that the user can search for events using key words.\
Test cases: \
`    ` - Empty string to check if KeyError is raised.\
Expected output: Console prints "Invalid input"\
Real output: "Invalid input" printed\
Result: Pass

`test` - Search for a premade "Test" event.\
Expected output: Console shows "Test" event along with its index number\
Real output: "0 Test"\
Result: Pass

`noEvent` - Search for an event that wasnt created.\
Expected output: Console shows that No event with the given name can be found\
Real output: "No events with the given keyword were found."\
Result: Pass

<br><br>
### Test suite 5:
Description: To test that the user can search for and then delete events using key words\
Test Cases:\
`test` - Search for a premade "Test" event.\
Expected output: Console shows "Test" event along with its index number\
Real output: "0 Test"\
Result: Pass

From here test that it deals with 3 types of inputs:\
`0` - Selecting the correct index and deleting the task.\
Output should print a message showing the success of deletion\
`2` - Selecting an index that does not exist.\
Output should print an Invalid Input message.\
`q` - Discarding any changes and returning to previous terminal.\
Console should return to asking for user input.\

`noEvent` - Search for an event that wasnt created.\
Expected output: Console shows that No event with the given name can be found\
Real output: "No events with the given keyword were found."\
Result: Pass

`    ` - Empty string to check if KeyError is raised.\
Expected output: Console prints "Invalid input"\
Real output: "Invalid input" printed\
Result: Pass

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