"""
CP1401 2022-2 Assignment 1
Program 1 – Pay Calculator
Student Name: <Low Yi Heng>
Date started: <20 December 2022>

Pseudocode:
BASIC_PAY = 45
EXPERIENCE_GIVES = 0.05
get work_hour
get experience_level
hourly_pay = (BASIC_PAY * (experience_level * EXPERIENCE_GIVES)) + BASIC_PAY
total_pay = work_hour * hourly_pay
display experience_level
display hourly_pay
display total_pay
"""
BASIC_PAY = 45
EXPERIENCE_GIVES = 0.05
work_hour = float(input("Number of hours worked :"))
experience_level = int(input("Experience level :"))
hourly_pay = (BASIC_PAY * (experience_level * EXPERIENCE_GIVES)) + BASIC_PAY
total_pay = work_hour * hourly_pay
print(f"Based on your Experience level ({experience_level}) : ")
print(f"Your hourly pay rate is ${hourly_pay}")
print(f"Your total pay is ${total_pay}")