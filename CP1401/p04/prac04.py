# 1)Error checking
"""
get worker_level
while worker_level < 1 or worker_level > 10
    display error message
    get worker_level
total_salary = worker_level * 5000
display worker_level and total_salary
"""
worker_level = int(input("Worker Level :"))
while worker_level < 1 or worker_level >10 :
    print("invalid worker level")
    worker_level = int(input("Worker Level :"))
total_salary = worker_level * 5000
print(f"With worker level {worker_level}, your salary is ${total_salary:,.2f}")

# 2)Number Sequences
"""
a)
for odd_number between 1 to 100
     display odd_number
"""
for odd_number in range (1,100,2) :
    print(odd_number)
"""
b)
for olympic_year between 1896 to 2022
     display olympic_year
"""
for olympic_year in range (1896,2022,4) :
    print(olympic_year ,end=" ")
"""
c)
for month between 1 to 13
    for test_day 1 and 14
         print test_day and month
"""
for month in range (1,13,1) :
    for test_day in ("1","14") :
        print(test_day ,"/" ,month ,sep="")

# 3) Menus
"""
display menu
get choice
while choice != s ,f ,q
     if choice == s
         display Smile
     else if choice == f
         display Frowny
     else
        display invalid choice
     display menu
     get choice
choice == q
display Farewell
"""
print("(S ,F ,Q)")
choice = input("Please enter your choice :").lower()
while choice != "q":
    if choice == "s" :
        print("SMILE")
    elif choice == "f" :
        print("FROWNY")
    else:
        print("invalid choice")
    print("S ,F ,Q")
    choice = input("Please enter your choice :").lower()
print("FAREWELL")

# 4) Accumulation
"""
(Average age)
SENTINEL = -1
NEXT_AGE = 1
total_age = 0
total_amount = 0
get age
while age > SENTINEL:
    total_age = total_age + age
    total_amount = total_amount + NEXT_AGE
    get age
if total_amount != 0:
    average_age = total_age / total_amount
    display average_age
else:
    display There is no age information.
"""
SENTINEL = -1
NEXT_AGE = 1
total_age = 0
total_amount = 0
age = int(input("Your age:"))
while age > SENTINEL:
    total_age += age
    total_amount += NEXT_AGE
    age = int(input("Your age:"))
if total_amount != 0:
    average_age = total_age / total_amount
    print(average_age)
else:
    print("There is no age information.")
"""
Smileys count
COUNT1 = 0
COUNT2 = 0
display menu
get choice
while choice != q
     if choice == s
         COUNT1 += 1
         display Smile
     else if choice == f
         COUNT += 1
         display Frowny
     else
        display invalid choice
     display menu
     get choice
display Farewell
display COUNT1 ,COUNT2
"""
COUNT1 = 0
COUNT2 = 0
print("(S ,F ,Q)")
choice = input("Please enter your choice :").lower()
while choice != "q":
    if choice == "s" :
        COUNT1 += 1
        print("SMILE")
    elif choice == "f" :
        COUNT2 += 1
        print("FROWNY")
    else:
        print("invalid choice")
    print("S ,F ,Q")
    choice = input("Please enter your choice :").lower()
print("FAREWELL")
print("SMILE :" ,COUNT1 ,"FROWNY :" ,COUNT2)

"""
Total numbers
TOTAL = 0
get number of people want
for count in range number of people want
    get age
    TOTAL = TOTAL + age
display number of people want ,TOTAL
"""
TOTAL = 0
number_people = int(input("How many numbers do you want to add up? "))
for count in range (number_people) :
    age = int(input("Age :"))
    TOTAL += age
print("The total of those" ,number_people ,"numbers is" ,TOTAL)

#5)Guessing Game
"""
SECRET = 6
get guess
 while guess != SECRET
    if guess < SECRET
        display guess higher
    else:
         display guess lower
    get guess
display You got it!
"""
SECRET = 6
COUNT = 0
guess = int(input("Guess a number: "))
while guess != SECRET:
    COUNT += 1
    if guess < SECRET:
          print("guess higher")
    else:
         print("guess lower")
    guess = int(input("Guess a number: "))
print("You got it in" ,COUNT ,"guessess !")

# 6)Nested Loops
"""
get number of rows
get number of columns
for i in range number of rows
    for j in range number of columns
        display j
"""
number_of_rows = int(input("Rows: "))
number_of_columns = int(input("Columns: "))
for i in range(number_of_rows):
    for j in range(number_of_columns):
        print(j, end=" ")
    print()
