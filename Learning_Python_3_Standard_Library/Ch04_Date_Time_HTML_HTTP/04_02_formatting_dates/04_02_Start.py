# Getting more control over formatting
from datetime import datetime
now = datetime.now()

# .strftime can be used to format the date
# %a abbreviated day; %A full day; %d day date
print(now.strftime("%a %A %d"), '\n')
# %b abbreviated month; %A full month; %d month date
print(now.strftime("%b %B %m"), '\n')

print(now.strftime("%A %B %d"), '\n')

# %y short year; %Y for long year
print(now.strftime("%y %Y"))

# hours, minutes, secs; %p for am/pm
print(now.strftime("%H:%M:%S %p"), '\n')

print(now.strftime("%H:%M:%S %A %B %d"))