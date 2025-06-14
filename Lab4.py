# 1. Get today's date and the date 5 days ago
from datetime import datetime, timedelta

current_date = datetime.now()
five_days_earlier = current_date - timedelta(days=5)

print("Today:", current_date)
print("5 Days Ago:", five_days_earlier)


# 2. Print yesterday's, today's, and tomorrow's dates
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


# 3. Remove microseconds from current datetime
from datetime import datetime

now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print("With Microseconds:", now)
print("Without Microseconds:", without_microseconds)


# 4. Find the difference between two datetime objects in seconds
from datetime import datetime

dt1 = datetime(2025, 6, 13, 12, 0, 0)
dt2 = datetime(2025, 6, 12, 10, 0, 0)
time_difference = dt1 - dt2
seconds_diff = time_difference.total_seconds()

print("Difference in Seconds:", seconds_diff)

