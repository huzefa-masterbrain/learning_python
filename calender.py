# from calendar import *
# year = int(input("Enter year: "))
# print(calendar(year))

from calendar import *

year = int(input("Enter year: "))
cal = TextCalendar()
print(cal.formatyear(year))
