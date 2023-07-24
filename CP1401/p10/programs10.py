def question_1():
    for i in range (40):
        print("-",end="")

# question_1()

def question_2():
    some_number = int(input("Number: "))
    if is_even(some_number):
        print(f"{some_number} is even")
    else:
        print(f"{some_number} is odd")

def is_even(num):
    return (num % 2) == 0

# question_2()

def question_3():
    name = get_nonempty_string("Name: ")
    birthplace = get_nonempty_string("Birthplace: ")
    print(f"your name is {name} and you were born in {birthplace}.")


def get_nonempty_string(prompt):
    string = input(prompt).title()
    while string == "":
        print("String is too short")
        string = input(prompt).title()
    return string

# question_3()

def question_4():
    minimum = int(input("Minimum number: "))
    maximum = int(input("Maximum number: "))
    while maximum <= minimum:
        print(f"Your maximum must be greater than {minimum}")
        maximum = int(input("Maximum number: "))
    numbers = []
    for number in range(minimum, maximum + 1):
        numbers.append(number)
    print(numbers)

# question_4()

def question_5():
    subjects = []
    subject = input("Enter subject code: ")
    while subject != "":
        if not is_valid_subject(subject):
            print("Invalid subject code")
        else:
            subjects.append(subject.upper())
        subject = input("Enter subject code: ")
    print(f"You do these {len(subjects)} subjects: ")
    subjects.sort()
    for subject in subjects:
        print(subject)
    if "CP1401" in subjects:
        print("You are cool")

def is_valid_subject(subject):
    if len(subject) != 6:
        return False
    if not subject[:2].isalpha():
        return False
    if not subject[2:].isdigit():
        return False
    return True

# question_5()
