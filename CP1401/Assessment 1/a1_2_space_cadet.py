"""
CP1401 2022-2 Assignment 1
Program 2 – Space Cadet Result
Student Name: <Low Yi Heng>
Date started: <20 December 2022>

Pseudocode:
FULL_MARK = 100
FAIL_MARK = 50
get practical_score
get exam_score
total_score = practical_score + exam_score
display total_score
if total_score < FAIL_MARK
    display fail
else
    if practical_score > exam_score
       display field agent
    else
        display desk officer
if total_score >= 90
   display honour roll
"""
FULL_MARK = 100
FAIL_MARK = 50
practical_score = float(input("Practical score (0-50) :"))
exam_score = float(input("Exam score (0-50) :"))
total_score = practical_score + exam_score
print(f"Your total score is {total_score} out of {FULL_MARK}")
if total_score < FAIL_MARK :
    print("You failed. Please try again next year.")
else :
    if practical_score > exam_score :
        print("You will become a field agent.")
    else :
        print("You will become a desk officer.")
if total_score >= 90 :
    print("Congratulations on making the honour roll!")