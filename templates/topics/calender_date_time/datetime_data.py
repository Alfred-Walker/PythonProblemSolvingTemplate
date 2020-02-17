"""calender_date_time parsing examples

Python calender_date_time module documentation:
   https://docs.python.org/2/library/datetime.html
"""

import datetime as dt


date = dt.datetime.now()
print(date)
# >>> 2020-02-17 11:23:42.487556


print(date.weekday())
# >>> one of weekday value belows
# (0:monday, 1:tuesday, 2:wednesday, 3:thursday, 4:friday, 5:saturday, 6:sunday)


date = dt.datetime(2020, 2, 17)
print(date)
print(date.day)
print(date.year)
print(date.month)
print(date.weekday())
# >>> 2020-02-17 00:00:00
# >>> 17
# >>> 2020
# >>> 2
# >>> 0


date = dt.datetime.strptime("2017-01-02 14:44", "%Y-%m-%d %H:%M")
print(date)
# >>> 2017-01-02 14:44:00


date = dt.datetime.strptime("2018/02/04 09:32:44", "%Y/%m/%d %H:%M")
print(date)
# >>> ValueError: unconverted data remains: :44
