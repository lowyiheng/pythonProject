"""
CP1401 2022-2 Assignment 1
Program 3 – Sleep Tracker
Student Name: <Low Yi Heng>
Date started: <20 December 2022>

Pseudocode:
SLEEP_DAY = 7
total_sleep_time = 0
day_number = 1
desirable_sleep_hour = 8
for sleep_day in range(1 ,SLEEP_DAY+1) :
    get sleep_time
    while sleep_time < 0 or sleep_time > 24 :
        display Invalid number
        get sleep_time
    day_number += 1
    total_sleep_time += sleep_time

total_time_expect  = SLEEP_DAY * desirable_sleep_hour
sleep_debt = total_time_expect - total_sleep_time

display total_time_expect
display total_sleep_time

if total_sleep_time < total_time_expect :
   display sleep_debt
else :
    display You are getting enough sleep. Keep it up!

"""
SLEEP_DAY = 7
total_sleep_time = 0
day_number = 1
desirable_sleep_hour = 8

for sleep_day in range(1 ,SLEEP_DAY+1) :
    sleep_time = float(input(f"Night {day_number} hours sleep :"))
    while sleep_time < 0 or sleep_time > 24 :
        print("Invalid number")
        sleep_time = float(input(f"Night {day_number} hours sleep :"))
    day_number += 1
    total_sleep_time += sleep_time

total_time_expect  = SLEEP_DAY * desirable_sleep_hour
sleep_debt = total_time_expect - total_sleep_time

print(f"Recommended total sleep is : {total_time_expect}")
print(f"Your total hours of sleep : {total_sleep_time}")

if total_sleep_time < total_time_expect :
   print(f"Your sleep debt over this time is: {sleep_debt}")
else :
    print("You are getting enough sleep. Keep it up!")