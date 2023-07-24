import random

def main():
    score = float(input("Score :"))
    while score >= 0 :
        grade = determine_grade(score)
        print(f"The score {score} is {grade}")
        score = float(input("Score :"))
    number_of_score = int(input("How many random score :"))
    for i in range (number_of_score) :
        score = random.randint(0,100)
        grade = determine_grade(score)
        print(f"{score} = {grade}")

def determine_grade(score):
    if score < 50 :
        return "F"
    elif score < 65 :
        return "P"
    elif score < 75 :
        return "C"
    elif score < 85 :
        return "D"
    else :
        return "HD"

main()
