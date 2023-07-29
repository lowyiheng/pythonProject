import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# I can see random numbers from 5 to 20

# What was the smallest number you could have seen, what was the largest?
# The smallest number i could seen is 5 and the largest number i could seen is 20

# What did you see on line 2?
# I can see random numbers 3, 5, 7, 9

# What was the smallest number you could have seen, what was the largest?
# The smallest number i could seen is 3 and the largest number i could seen is 9

# Could line 2 have produced a 4?
# No because the number start from 3 and the step size is 2 so the next number will be 5.

# What did you see on line 3?
# I can see random numbers from 2.5 to 5.5

# What was the smallest number you could have seen, what was the largest?
# The smallest number i could seen is 2.5 and the largest number i could seen is 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

random_number = random.randint(1, 100)
print(random_number)
