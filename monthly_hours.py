# This program will print the total number of hours for each
# of two pay periods for the month.
import calendar
from datetime import datetime
import sys

def pay_period_hours(week):
    global yy, mm
    
    last_day = calendar.monthrange(int(yy), int(mm))[1] + 1

    if week == 1:
        day_range = range(1,16)
    else:
        day_range = range(16, last_day)

    total_hours = 0

    for day in day_range:
        day_num = datetime.fromisoformat(f'{yy}-{mm}-{day:02}').timetuple().tm_wday
        if  day_num < 5:
            total_hours += 8
         
    return total_hours

if len(sys.argv) == 1:
    yy, mm, _, _, _, _, _, _, _ = datetime.now().timetuple()
else:
    yy, mm = sys.argv[1].split('-')

print(f" First pay period: {pay_period_hours(1)} hours")
print(f"second pay period: {pay_period_hours(2)} hours")
