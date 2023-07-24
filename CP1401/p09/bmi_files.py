def question_7():
    number_of_people = int(input("Enter the number of people: "))
    bmis = []
    for i in range(number_of_people):
        height, weight = get_user_input()
        bmi = calculate_bmi(weight, height)
        bmis.append(bmi)
    write_bmis_to_file(bmis)
    print("BMIs have been written to bmis.txt.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_user_input():
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kg: "))
    return height, weight

def write_bmis_to_file(bmis):
    with open('../bmis.txt', 'w') as file:
        for bmi in bmis:
            file.write(str(bmi) + '\n')

question_7()