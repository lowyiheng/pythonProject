def question_1():
    data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",

                    "Something else that's very important = 9.2%", "x = 42%"]
    for string in data_strings:
        print(float(string[string.find("=")+2: len(string)-1]))

question_1()

"""
NEXT_YEAR = 2024

function main()
    get date_of_birth
    year_of_birth = year in date_of_birth
    age_next_year = NEXT_YEAR - year_of_birth
    print year_of_birth, age_next_year, NEXT_YEAR
"""
NEXT_YEAR = 2023

def question_2():
    date_of_birth = input("DOB: ")
    year_of_birth = int(date_of_birth[-4:])
    age_next_year = NEXT_YEAR - year_of_birth
    print(f"You were born in {year_of_birth}. \nYou will turn {age_next_year} in {NEXT_YEAR}")

question_2()

"""

"""
def question_3():
    subject_code = input("Enter subject code: ").upper()
    while subject_code != "":
        if subject_code[0:2] == "CP":
            it_string = " IT"
        else:
            it_string = ""
        if subject_code[2:3] == "1":
            year_string = "first-year"
        elif subject_code[2:3] == "2":
            year_string = "second-year"
        elif subject_code[2:3] == "3":
            year_string = "third-year"
        else:
            year_string = "Masters or other"
        print(f"That is a {year_string}{it_string} subject.")
        subject_code = input("Enter subject code: ")
        print()

question_3()