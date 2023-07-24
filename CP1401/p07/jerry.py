"""
MILES_TO_KILOMETRES = 1.60934
function main
    user_speed = get_valid_number("speed in mph")
    speed_limit = get_valid_speed_limit("speed in kph")
    speed_in_kilometre = miles_to_kilometre(user_speed)
    print fine
"""
MILES_TO_KILOMETRES = 1.60934
def main():
    """determine the penalty fee."""
    user_speed = get_valid_number()
    speed_limit = get_valid_speed_limit()
    speed_in_kilometre = miles_to_kilometre(user_speed)
    over_speed_fine(speed_limit ,speed_in_kilometre)

def get_valid_number():
    """get speed in mph."""
    user_speed = float(input("Please enter your speed (mph):"))
    while user_speed < 0 :
        print("invalid number")
        user_speed = float(input("Please enter your speed (mph):"))
    return user_speed

def get_valid_speed_limit():
    """get speed limit in kph."""
    speed_limit = float(input("Please enter speed limit (kph):"))
    while speed_limit < 0 :
        print("invalid number")
        speed_limit = float(input("Please enter speed limit (kph):"))
    return speed_limit

def miles_to_kilometre(user_speed):
    """get speed in kph."""
    speed_in_miles = user_speed
    speed_in_kilometre = speed_in_miles * MILES_TO_KILOMETRES
    return speed_in_kilometre

def over_speed_fine(speed_limit ,speed_in_kilometre):
    """get the fine value."""
    over_speed = speed_in_kilometre - speed_limit
    if over_speed <= 0 :
        print("no penalty")
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

main()