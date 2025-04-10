# Calendar Module
from datetime import datetime, timedelta
import calendar
now = datetime.now()

#timedelta() allows to change an atrribute of the time by a set ammount
testDate = now + timedelta(days=2)
teaTime = now + timedelta(hours=4)
myFirstLinkedInCourse = now - timedelta(weeks=3)

print(testDate.date())
print(teaTime.time())
print(myFirstLinkedInCourse.date(), '\n')

# Dates can be compared (past<Future)
if testDate > myFirstLinkedInCourse:
    print("Comparison works", '\n')

# The calendar of months can be called with calender.month(yr, month)
cal = calendar.month(2006, 5)
print(cal)
# The weekday of a certain date can be called w/ calender.weekday(yr, month, day)
cal2 = calendar.weekday(2006, 5, 20)
print(cal2) # 0:Mon; 1:Tue etc.

# You can also determin if certain years were leap or not
print(calendar.isleap(1999))
print(calendar.isleap(2000))
print(calendar.isleap(2100))