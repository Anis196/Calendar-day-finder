## Calendar Day Finder
This Python script calculates the day of the week for a given date. By providing a date, month, and year, the script determines which day of the week the given date falls on.

### How to Use
**Input:**
- date: An integer representing the day of the month.
- month: A string representing the month (e.g., "January").
- year: An integer representing the year.

**Output:**
The script outputs the day of the week corresponding to the provided date.

### Code Explanation
The calendar_1 function performs the following steps:

**Century Calculation:**
Determines the century of the given year and calculates an initial odd day value.

**Remaining Years Calculation:**
Calculates the remaining years within the century and further adjusts the odd day value based on the number of leap years and ordinary years.

**Month Adjustment:**
Adjusts the odd day value based on the cumulative number of days before the start of the given month.

**Date Adjustment:**
Further adjusts the odd day value by adding the given date.

**Day Mapping:**
Maps the final odd day value to the corresponding day of the week.

### How to Run
1. Ensure you have Python installed on your system.
2. Save the script in a file, for example, ``calendar_day_finder.py``.
3. Open a terminal or command prompt.
4. Navigate to the directory where the script is saved.
5. Run the script using the command: ``python calendar_day_finder.py``.
6. Enter the date, month, and year when prompted.

For example:
```
Enter date: 23
Enter month: July
Enter year: 2024
The Day on 23 July 2024 was / is Tuesday
```

### License
This project is licensed under the MIT ``License``.

### Contributions
Feel free to fork this repository, make your changes, and submit a pull request. All contributions are welcome!

**Note: No library has been used for performing any of the operations, its raw logic:P I made this short program just for fun and as a way to always remember the concept and logic behind Calendar related problems.**
