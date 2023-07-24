"""
import random
numbers = empty list
get random number
get maximum number
for i in range random number
    number = random between (0,maximum number)
    add number to numbers
display numbers
display min(numbers)
display max(numbers)
number = random choice in numbers
display numbers
reverse numbers
display numbers
sort numbers
display numbers
"""
import random
numbers = []
random_number = int(input("How many random numbers :"))
maximum_number = int(input("Maximum number :"))
for i in range (random_number) :
     number = random.randint(0 ,maximum_number)
     numbers.append(number)
print(f"The numbers are :{numbers}")
print(f"The minimum is {min(numbers)}")
print(f"The maximum is {max(numbers)}")
number = random.choice(numbers)
print(f"A randomly chosen number is {number}")
numbers.reverse()
print(f"The numbers reversed are {numbers}")
numbers.sort()
print(f"The numbers sorted are {numbers}")

