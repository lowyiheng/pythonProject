def main():
    dose = get_valid_number("Dose: ", 0, 100)
    coffee_yield = get_valid_number("Yield: ", 0, 200)
    ratio = coffee_yield / dose
    style = determine_coffee_style(ratio)
    print(f"1:{ratio} is considered {style}")


def determine_coffee_style(ratio):
    if ratio < 2:
        return "ristretto"
    elif ratio < 3:
        return "normale"
    else:
        return "lungo"


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number

def check_coffee():
    style = determine_coffee_style(1)
    print(style)  # This should be ristretto
    style = determine_coffee_style(2)
    print(style)  # This should be normale
    style = determine_coffee_style(13.5)
    print(style)  # This should be lungo

check_coffee()
main()