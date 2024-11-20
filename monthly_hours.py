# This program will print the total number of hours for each
# of two pay periods for the month.

# Required modules
import calendar
from datetime import datetime
import sys

# This calculates the number of hours for the given week of the month.
#  Week 1 - Dates 1-15
#  Week 2 - Dates 16-last
def pay_period_hours(week):
    global yy, mm

    # Get the last day of the month.  calendar.monthrange returns a tuple containing
    # the first day of the month (0-6) and the date of the last day (29, 30, 31)
    # i.e. 2024-11 returns (4, 30).  4 is Friday (Monday is 0, Sunday is 6).  30 is the
    # last day of the month (11)
    last_day = calendar.monthrange(int(yy), int(mm))[1] + 1

    # Set the day range based on the week.
    if week == 1:
        day_range = range(1,16)
    else:
        day_range = range(16, last_day)

    # Initialize total hours to zero
    total_hours = 0

    # Loop through each day in day_range.  If number of the day is between 0 (Monday)
    # and 4 (Friday), inclusive, add 8 to the total hours.
    #
    # datetime.fromisoformat requires a string formatted as "yyyy-mm-dd".  The date is
    # converted to a time tuple.  day_num is set to the number of the weekday (tm_wday).
    for day in day_range:
        day_num = datetime.fromisoformat(f'{yy}-{mm:02}-{day:02}').timetuple().tm_wday
        if  day_num < 5:
            total_hours += 8

    return total_hours

# If no command-line parameters, use the current date.
# The timetuple contains 9 values.  Only year and month are
# required.  The rest of the values are ignored (hence the '_' characters)
if len(sys.argv) == 1:
    yy, mm, _, _, _, _, _, _, _ = datetime.now().timetuple()
else:
    # If year/month were passed on the command line, split the string
    # in to year and month (delimited by '-')
    yy,mm = sys.argv[1].split('-')
    yy = int(yy)
    mm = int(mm)
    if mm > 12:
        print(f"The specified month ({mm}) must be between 1 and 12.")
        sys.exit()

# Print the hours for each pay period.  Month name is
# derived from a list of month names indexed by 'mm'
print(f"Hours for {list(calendar.month_name)[mm]} {yy}")
print('-' * 27)
print(f" First pay period: {pay_period_hours(1)}")
print(f"second pay period: {pay_period_hours(2)}")
