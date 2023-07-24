# 1.Tax
"""
TAX_RATE_LOW = 0.02
TAX_RATE_MIDDLE = 0.05
TAX_RATE_HIGH = 0.1
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_MIDDLE = 500
TAX_THRESHOLD_HIGH = 1000
get income
if income < TAX_THRESHOLD_LOW
    total_tax = 0
else if income < TAX_THRESHOLD-MIDDLE
     total_tax = income * TAXE_RATE_LOW
else if income < TAX_THRESHOLD_HIGH
     total_tax = income * TAX_RATE_MIDDLE
else
    total_tax = income * TAX_RATE_HIGH
take_home_pay = income - total_tax
display total_tax, take_home_pay
"""
TAX_RATE_LOW = 0.02
TAX_RATE_MIDDLE =0.05
TAX_RATE_HIGH = 0.1
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_MIDDLE = 500
TAX_THRESHOLD_HIGH = 1000
print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))
if income < TAX_THRESHOLD_LOW:
    total_tax = 0
elif income < TAX_THRESHOLD_MIDDLE:
     total_tax = income * TAX_RATE_LOW
elif income < TAX_THRESHOLD_HIGH:
     total_tax = income * TAX_RATE_MIDDLE
else:
    total_tax = income * TAX_RATE_HIGH
take_home_pay = income - total_tax
print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")

# 2.Car Insurance
"""
get applicant_age
if applicant_age < 18
   display Hire refused
else if applicant_age < 25
        display Insurance required
else 
    display Insurance not required
"""
applicant_age = float(input("Please enter your age :"))
if applicant_age < 18 :
    print("Hire Refused")
elif applicant_age < 25 :
    print("Insurance Required")
else:
    print("Insurance not required")

# 3.Simple Password Checker
"""
get password
if password == PASSWORD
    display Access Granted
else:
    display Access Denied
"""
PASSWORD = "Hi123"
password = input("Please enter your password :")
if password == PASSWORD :
    print("Access Granted")
else:
     print ("Access Denied")

# 4.Dog Years
"""
get human_year
if human_year <= 2
    dog_year = human_year * 10.5
else
    dog_year = (human_year - 2) * 4 + (10.5 * 2)
display dog_year
"""
human_year = float(input("please enter your dog's human age :"))
if human_year <= 2 :
    dog_year = human_year * 10.5
else:
    dog_year = (human_year - 2) * 4 + (10.5 * 2)
print("Age in dog years is :" , dog_year)

# 5.Rock of Ages
"""
get user_age
if user_age < 0 and user_age >120 :
    display invalid age
else if user_age <= 30
    display you still young just do whatever you like
else if user_age <= 60
     display eventhough you are busy but don't forget to spend time with your family
else if user_age <= 90
     display don't forget to do exercise to keep fit
else
     display congratulations and hope your next fill in can get a invalid age
"""
user_age = float(input("Please enter your age :"))
if user_age < 0 and user_age >120 :
    print("invalid age")
elif user_age <= 30:
    print("You still young just do whatever you like")
elif user_age <= 60 :
     print("Eventhough you are busy but don't forget to spend time with your family")
elif user_age <= 90 :
     print("Don't forget to do exercise to keep fit")
else :
     print("Congratulations and hope your next fill in can get a invalid age")

# 6.Speeding Fines
"""
get user_speed , speed_limit
over_speed = user_speed - speed_limit
if over_speed < 13
   display penalty amount $177
else if over_speed <= 20
   display penalty amount $266
else if over_speed <= 30
   display penalty amount $444
else if over_speed <= 40
   display penalty amount $622
else 
   display penalty amount $1245 
"""
user_speed = float(input("Please enter your speed :"))
speed_limit = float(input("Please enter the speed limit :"))
over_speed = user_speed - speed_limit
if over_speed < 13 :
   print("penalty amount $177")
elif over_speed <= 20 :
   print("penalty amount $266")
elif over_speed <= 30 :
   print("penalty amount $444")
elif over_speed <= 40 :
   print("penalty amount $622")
else :
   print("penalty amount $1245")

