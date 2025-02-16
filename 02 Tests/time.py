# Getting current date and time using now().
import os
os.system("cls")

from datetime import datetime

now = datetime.now() # current date and time

#print("TIME: ", timenow, "\n\n\n")

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

print("year", type(year))
print("month", type(month))
print("day", type(day))
print("time", type(time))
