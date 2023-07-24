"""CP1401 - Practical 8 - Debugging."""

# Debug program 1 - friends' names
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(0, len(names)):
    print(f"{i + 1}. {names[i]}")
last_number = len(names)
print(f"The last name (number {last_number}) is {names[last_number - 1]}")

# Problem(s) for program 1:
# ?line 6 range define incorrect
#    line 9 names[last_number] is out of range

# Fixed code for program 1:
# change the range from 1 to 0
# add + 1 in line 7
# add - 1 in line 9

# Debug program 2 - title-casing country names
countries = ["australia", "new zeaLAND", "India"]
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)  # country names should be in title-case now

# Problem(s) for program 2:
# ?tuples are immutable

# Fixed code for program 2:
# change tuples to list