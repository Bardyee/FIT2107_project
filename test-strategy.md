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

<br><br>
### Test suite 2:

<br><br>
### Test suite 3:
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
### Test suite 4:
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