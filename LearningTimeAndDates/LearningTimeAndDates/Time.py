#What about Times?
#It is called datetime, so yes, it can stores times.

import datetime

currentTime = datetime.datetime.now()
print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)
print(datetime.datetime.strftime(currentTime, "%H:%M %p"))

# %H Hours (24 hr clock)
# %I Hours (12 hr clock)
# %p AM or PM
# %m Minutes
# %S seconds

currentDate = datetime.datetime.now()
print(currentDate.minute)
