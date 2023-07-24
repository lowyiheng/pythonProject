# All Together Now
"""
print menu
get choice
while choice != quit
    if choice == 'i'
        print instructions
    else if choice == 'c'
        get number_of_products
        while number_of_products < 0
            print error message
            get number_of_products
        get price
        while price < 0
            print error message
            get price
        total = number_of_products * item_price
        if number_of_products > 5
            total = total * 0.9
        print total
    else
        print "Invalid choice"
    print menu
    get choice
print farewell message
"""
DISCOUNT_THRESHOLD = 5
print("(I)nstructions")
print("(C)alculate")
print("(Q)uit")
choice = input("Choice :").lower()
while choice != "q" :
    if choice == "i" :
        print("Enter the number of products you want to buy and your chosen price.")
        print("If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
    elif choice == "c" :
        number_of_product = int(input("Number Of Product :"))
        while number_of_product < 0 :
            print("invalid")
            number_of_product = int(input("Number Of Product :"))
        item_price = float(input("Price :"))
        while item_price < 0 :
            print("invalid")
            item_price = float(input("Price :"))
        total_price = number_of_product * item_price
        if number_of_product > DISCOUNT_THRESHOLD :
            total_price = (number_of_product * item_price) * 0.9
        print(f"{number_of_product} x {item_price} products = ${total_price}")
    else :
        print("invalid")
    print("(I)nstructions")
    print("(C)alculate")
    print("(Q)uit")
    choice = input("Choice :").lower()
print("Farewell")

