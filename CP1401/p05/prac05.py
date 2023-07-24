# 1)Percentage change
"""
get original_value
get change_value
new_value = original_value + (change_value * original_value)
display original_value ,change_value,new_value
"""
original_value = float(input("original :"))
change_value = float(input("Change :"))
new_value = original_value + (change_value * original_value)
print(f"Original: {original_value} ,Change: {change_value} ,Result: {new_value}")

# 2)Time of day
"""
TIME_OF_NOON = 12
get time_of_day ,coming_or_going
if time_of_day <= TIME_OF_NOON :
   time_now = "befor noon"
else :
    time_now = "after noon"
if coming_or_going == "coming" :
    word_shown = "hi"
else :
    word_shown = "bye"
display time_now ,coming_or_going ,word_shown
"""
TIME_OF_NOON = 12
time_of_day = int(input("time of day (0-23 hours) :"))
coming_or_going = input("are you coming or going :")
if time_of_day <= TIME_OF_NOON :
   time_now = "befor noon"
else :
    time_now = "after noon"
if coming_or_going == "coming" :
    word_shown = "hi"
else :
    word_shown = "bye"
print(f"It is {time_now} and you are {coming_or_going}. {word_shown}")

# 3)Coffee orders
"""
SMALL_PRICE = 3
MEDIUM_PRICE = 4
LARGE_PRICE = 5
COFFEE_TYPE_PRICE = 1
get coffee_size,coffee_type
if coffee_size == small
    coffee_price = 3
else if coffee_size == medium
    coffee_price = 4
else
    coffee_price = 5
if coffee_type != black
    coffee_price = coffee_price + 1
display coffee_price
"""
SMALL_PRICE = 3
MEDIUM_PRICE = 4
LARGE_PRICE = 5
COFFEE_TYPE_PRICE = 1
coffee_size = str(input("please select your coffee size(Small, Medium, Large):")).lower()
coffee_type = str(input("please select your coffee type(white or black):")).lower()
if coffee_size == "small":
    coffee_price = SMALL_PRICE
elif coffee_size == "medium":
    coffee_price = MEDIUM_PRICE
else:
    coffee_price = LARGE_PRICE
if coffee_type != "black":
    coffee_price += COFFEE_TYPE_PRICE
print(f"Your price is ${coffee_price}")

# 4)Coffee orders with error-checking
"""
SMALL_PRICE = 3
MEDIUM_PRICE = 4
LARGE_PRICE = 5
COFFEE_TYPE_PRICE = 1
get coffee_size
while coffee_size != "small" and coffee_size != "medium" and coffee_size != "large"
     display invalid
     get coffee_size
while coffee_type != "black" and coffee_type != "white"
     display invalid
     get offee_type
if coffee_size == small
    coffee_price = 3
else if coffee_size == medium
    coffee_price = 4
else
    coffee_price = 5
if coffee_type != black
    coffee_price = coffee_price + 1
display coffee_price
"""
SMALL_PRICE = 3
MEDIUM_PRICE = 4
LARGE_PRICE = 5
COFFEE_TYPE_PRICE = 1
coffee_size = str(input("please select your coffee size(Small, Medium, Large):")).lower()
while coffee_size != "small" and coffee_size != "medium" and coffee_size != "large" :
    print("invalid")
    coffee_size = str(input("please select your coffee size(Small, Medium, Large):")).lower()
coffee_type = str(input("please select your coffee type(white or black):")).lower()
while coffee_type != "black" and coffee_type != "white":
    print("invalid")
    coffee_type = str(input("please select your coffee type(white or black):")).lower()
if coffee_size == "small":
    coffee_price = SMALL_PRICE
elif coffee_size == "medium":
    coffee_price = MEDIUM_PRICE
else:
    coffee_price = LARGE_PRICE
if coffee_type != "black":
    coffee_price += COFFEE_TYPE_PRICE
print(f"Your price is ${coffee_price}")

# 5)Accumulation
"""
total_value = 0
get low_value, high_value
while low_value > high_value
    display invalid
    get low_value, high_value
for i in range(low_value, high_value+1)
    display i
    total_value = total_value + i
display total_value
"""
total_value = 0
low_value = int(input("Enter low value:"))
high_value = int(input("Enter high value:"))
while low_value > high_value:
    print("Invalid, enter again!")
    low_value = int(input("Enter low value:"))
    high_value = int(input("Enter high value:"))
for i in range(low_value, high_value+1):
    print(i, end=" ")
    total_value += i
print("Total:" ,total_value)




