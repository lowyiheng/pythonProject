"""
CP1401 2022-1 Assignment 2
Market Garden Simulator
Student Name : Low Yi Heng
Date started : 24 January 2023

function main
       food = 0
       days = 0
       plants = ["Parsley", "Sage", "Rosemary", "Thyme"]
       print_welcome_message()
       user_input = ""
       while user_input.lower() != 'q':
            display days ,length of plants ,foods
            display_manu()
            get user input
            if user_input.lower() not in "wdaq":
                display Invalid choice
            elif user_input.lower() == "w":
                random rainfall from 0 to 100
                display rainfall
                if rainfall > 30:
                    days += 1
                    for plant in plants:
                        food = random [(rainfall / 200 * length of the plant) ,(rainfall / 100 * length of the plant)]
                        foods += food
                        display plant ,food
                else:
                    random dead_plant from plants
                    remove dead_plant from plants
                    display dead_plant
                    for plant in plants:
                        food = 0
                        display plant ,food
            elif user_input.lower() == "d":
                display plant in plants
            elif user_input.lower() == "a":
            get plant_name
            while True:
                if length of the plant_name == 0:
                    display Invalid plant name
                elif plant_name in plants:
                    display plant_name
                elif length of the plant_name > foods:
                    display plant_name ,length of the plant_name ,food
                    break
                else:
                    add plant_name to plants
                    foods -= length of the plant_name
                    break
                get plant_name
    print_finish_message(plants, foods, days)

function print_finish_message(plants, foods, days)
    display You finished with these plants
    display plant in plants
    display days ,length of the plants ,foods
    display Thank you for simulating. Now enjoy some real plants.

"""
import random

def main():
    foods = 0
    days = 0
    plants = ["Parsley", "Sage", "Rosemary", "Thyme"]
    print_welcome_message()
    user_input = ""
    while user_input.lower() != 'q':
        print(f"After {days} days, you have {len(plants)} plants and your total food is {foods}.")
        display_menu()
        user_input = input("Choose: ")
        if user_input.lower() not in "wdaq":
            print("Invalid choice")
            continue
        elif user_input.lower() == "w":
            rainfall = random.randint(0, 100)
            print(f"Rainfall: {rainfall}mm")
            if rainfall > 30:
                days += 1
                for plant in plants:
                    food = random.randint(int(rainfall / 200 * len(plant)), int(rainfall / 100 * len(plant)))
                    foods += food
                    print(f"{plant} produced {food}, ", end="")
                print()
            else:
                dead_plant = random.choice(plants)
                plants.remove(dead_plant)
                print(f"Sadly, your {dead_plant} plant has died.")
                for plant in plants:
                    food = 0
                    print(f"{plant} produced {food}, ", end="")
                print()
        elif user_input.lower() == "d":
            [print(plant, end=", ") for plant in plants]
            print()
        elif user_input.lower() == "a":
            plant_name = input("Enter plant name: ")
            while True:
                if len(plant_name) == 0:
                    print("Invalid plant name")
                elif plant_name in plants:
                    print(f"You already have a {plant_name} plant")
                elif len(plant_name) > foods:
                    print(f"{plant_name} would cost {len(plant_name)} food. With only {foods}, you can't afford it.")
                    break
                else:
                    plants.append(plant_name.title())
                    foods -= len(plant_name)
                    break
                plant_name = input("Enter plant name: ")
    print_finish_message(plants, foods, days)

def print_welcome_message():
    print("Welcome to my garden.")
    print("Plants cost and generate food according to their name length (e.g., Sage plants cost 4).")
    print("You can buy new plants with the food your garden generates.")
    print("You get up to 128 mm of rain per day. Not all plants can survive with less than 32.")
    print("Enjoy :)")
    print("Would you like to load your plants from plants.txt (Y/n)?")
    print("You start with these plants:")
    print("Parsley, Sage, Rosemary, Thyme,")
    print()

def print_finish_message(plants, foods, days):
    print("You finished with these plants:")
    [print(plant, end=", ") for plant in plants]
    print()
    print(f"After {days} days, you have {len(plants)} plants and your total food is {foods}.")
    print("Thank you for simulating. Now enjoy some real plants.")

def display_menu():
    print("(W)ait")
    print("(D)isplay plants")
    print("(A)dd new plant")
    print("(Q)uit")

main()