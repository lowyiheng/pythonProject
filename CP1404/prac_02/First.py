MINIMUM_PASSWORD = 0

password = input("Please enter your passwords: ")
while len(password) <= MINIMUM_PASSWORD :
    print("invalid password")
    password = input("Please enter your passwords: ")
asterisks = len(password) * "*"
print(asterisks)

