def main():
    number = get_number()
    remainder = get_remainder(number)
    print(f"Parity of {number} should be {remainder} : {get_remainder(number)}")

def get_number():
    number = int(input("Number :"))
    return number

def get_remainder(number):
    remainder = number % 2
    return remainder

main()
print(get_remainder(4))
print(get_remainder(41))
print(get_remainder(28))
print(get_remainder(27))
