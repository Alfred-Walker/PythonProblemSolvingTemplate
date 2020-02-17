"""calendar data examples

Python calendar module documentation:
   https://docs.python.org/2/library/calendar.html
"""

import calendar


weekday = calendar.weekday(2020, 2, 17)
print(weekday)
# >>> 0
# (0:monday, 1:tuesday, 2:wednesday, 3:thursday, 4:friday, 5:saturday, 6:sunday)

monthrange = calendar.monthrange(2020, 2)
print(monthrange)
# >>> (5, 29)
# (weekday of first day(e.g. 5 is saturday), last day of the month)
