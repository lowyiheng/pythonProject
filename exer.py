out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2
file = open("name.txt", "r")
name = file.read().strip()
file.close()
print("Your name is", name)

# 3
file = open("numbers.txt", "r")
first_number = int(file.readline())
second_number = int(file.readline())
print(first_number + second_number)

# 4
total = 0
file = open("numbers.txt", "r")
for line in file:
    number = int(line)
    total += number
file.close()
print(total)