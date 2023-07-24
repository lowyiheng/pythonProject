# Example
"""
get original_price and surcharge_rate
extra charge = original_price * surcharge_rate
total_price = original_price + extra_charge
display total_price
"""


# 1.Discount Price
"""
DISCOUNT_RATE = 0.2
get original_price
discount = original_price * DISCOUNT_RATE
new_price = original_price – discount
print new_price
"""

DISCOUNT_RATE = 0.2
original_price = float(input("Original Price:$"))
discount = original_price * DISCOUNT_RATE
new_price = original_price - discount
print ("The new price is $", new_price,sep="")


# 2.Kilometres To Miles
"""
KILOMETRES_TO_MILES = 0.621371
get distance_in_kilometres
distance_in_miles = distance_in_kilometres * KILOMETRES-TO-MILES
print distance_in-miles
"""

KILOMETRES_TO_MILES = 0.621317
distance_in_kilometres = float(input("Distance in kilometres:"))
distance_in_miles = distance_in_kilometres * KILOMETRES_TO_MILES
print ("Distance in miles:" ,distance_in_miles ,sep="")

# 3.Holiday Cost
"""
get daily_food_cost ,daily_activities_cost ,number_of_days
total_trip_cost = (daily_food_cost + daily_activities_cost + 75$) * number_of_days
print total_trip_cost
"""

HOTEL_COST = 75
daily_food_cost = float(input("Daily food cost :$"))
daily_activities_cost = float(input("Daily activities cost :$"))
number_of_days = float(input("Number of days :"))
total_trip_cost = (daily_food_cost + daily_activities_cost + HOTEL_COST) * number_of_days
print ("The trip will cost $" ,total_trip_cost ,sep="")


# 4.Deep Sleep Calculation(Percentage)
"""
MINUTES_TO_SECONDS = 60
PERCENTAGE = 100
get total_sleep_in_seconds ,deep_sleep_in_seconds
deep_sleep_minutes = deep_sleep_in_seconds // MINUTES_TO_SECONDS
deep_sleep_second = deep_sleep_in_seconds % MINUTES_TO_SECONDS
total_sleep_minutes = total_sleep_in_seconds // MINUTES_TO_SECONDS
total_sleep_minutes = total_sleep_in_seconds % MINUTES_TO_SECONDS
percentage_of_deep_sleep = (deep_sleep_in_seconds / total_sleep_in_seconds) * PERCENTAGE
print deep_sleep_second , deep_sleep_second
print total_sleep_minutes , total_sleep_minutes
print percentage_of_deep_sleep
"""

MINUTES_TO_SECONDS = 60
PERCENTAGE = 100
total_sleep_in_seconds = int(input("Total sleep in seconds:"))
deep_sleep_in_seconds = int(input("Deep sleep in seconds:"))
deep_sleep_minutes = deep_sleep_in_seconds // MINUTES_TO_SECONDS
deep_sleep_seconds = deep_sleep_in_seconds % MINUTES_TO_SECONDS
total_sleep_minutes = total_sleep_in_seconds // MINUTES_TO_SECONDS
total_sleep_seconds = total_sleep_in_seconds % MINUTES_TO_SECONDS
percentage_of_deep_sleep = (deep_sleep_in_seconds / total_sleep_in_seconds) * PERCENTAGE
print("")
print("")
print ("Deep sleep : " ,deep_sleep_minutes ,"m" ,deep_sleep_seconds ,"s" ,sep="")
print ("Total sleep : " ,total_sleep_minutes ,"m" ,total_sleep_seconds ,"s" ,sep="")
print ("Percentage : " ,percentage_of_deep_sleep ,"%" ,sep="")
