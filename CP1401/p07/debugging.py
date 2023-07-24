"""CP1401 - Practical 7 - Debugging.
The "demo" problem shows how the answers should be written.
Follow the example and template to answer the questions (find and fix problems) below.
"""


def demo():
    """Problematically do list duplication and reversing."""
    things = [1, 2, 3, 4]
    new_things = dupli_reversify(things)
    print(new_things)
def dupli_reversify(x):
    """Create mirrored list from passed-in list, e.g., [0, 1] -> [0, 1, 1, 0]."""
    return x + x.reverse()

# Problem(s) for demo program:
# x.reverse() modifies the list in-place and evaluates to None (it does not evaluate to a list).
# x (list) + None gives a TypeError
# (Notice that the answer is about the bug/problem, not about style, names, formatting, etc.)

# Fixed code for demo program:
def dupli_reversify(x):
    """Create mirrored list from passed-in list, e.g., [0, 1] -> [0, 1, 1, 0]."""
    return x[:] + x[::-1]
    # or
    # return x + list(reversed(x))
# (Notice that the answer includes the whole fixed function. No style/naming issues have been improved.)

# Questions start here:

def main_1():
    """Determine the parity of a user's number."""
    number = int(input("Enter number: "))
    parity = calculate_parity(number)
    print(parity)

def calculate_parity(number):
    """Calculate the parity (0 or 1) of number passed in."""
    return (number%2)

# Problem(s) for program 1:
# missing the argument.

# Fixed code for program 1:
# add the argument in line 34 (calculate_parity(number) :)

def main_2():
    """Print numbers from 0 up to the user's input multiplied by 2."""
    # E.g., if input is 12, should print 0 2 4 6 8 10 12 14 16 18 20 22 24
    numnums = int(input("How many: "))
    for i in range (0 ,numnums * 2 + 1 ,+ 2):
        print(i ,end=" ")

# Problem(s) for program 2:
# logical error

# Fixed code for program 2:
# add int in line 50
# add range and add parameter in for loop

def main_3():
    """Determine the area of a rectangle."""
    length, width = 12, 10
    area = calculate_area(length, width)
    print(f"The area is {area}")

def calculate_area(length, width):
    """Calculate the area of a rectangle from its dimensions."""
    result = length * width
    return result

# Problem(s) for program 3:
# wrong argument in function
# didn't return the result

# Fixed code for program 3:
# replace the correct argument
# add return in line 70


def main_4():
    """Show how old a person will be in the future."""
    INCREMENT = 10
    age = int(input("Age: "))
    while age < 0 and age > 120:
        print("Invalid age")
        age = int(input("Age: "))
    next_age = age + INCREMENT
    print(f"In {INCREMENT} years, you will be {next_age} years old!")

# Problem(s) for program 4:
# no calculation

# Fixed code for program 4:
# add calculation in line 88

# demo()
# main_1()
main_2()  # Note: these are not good names; just something to reduce the amount of copying we need to do
# main_3()
# main_4()