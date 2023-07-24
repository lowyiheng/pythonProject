"""
count = 1
scores = empty list
main function
     for i in range
         get score
         while score < 0 or score > 100
            display ivalid score
            get score
         add score to scores
     for score in scores
         grade = determine_grade(score)
         display score ,grade
     average_score = get_average_score(scores)
     display average_score
     get_trend(average_score ,scores)

get_trend function
    if average_score < scores[-1]:
        display The trend is positive
    else:
        display The trend is negative


get_average_score function
    average_score = sum of the scores / length of the scores
    return average_score


determine_grade function
    if score < 50:
        return "N"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    else:
        return "HD"

main()
"""
def main():
    """display grade ,average score and trend."""
    count = 1
    scores = []
    for i in range(1, 4 + 1):
        score = float(input(f"Score {i} :"))
        while score < 0 or score > 100:
            print("invalid score")
            score = float(input(f"Score {i} :"))
        scores.append(score)
    for score in scores:
        grade = determine_grade(score)
        print(f"Score {count} was {score}, which is {grade}")
        count += 1
    average_score = get_average_score(scores)
    print(f"The average score was {average_score}")
    get_trend(average_score, scores)


def get_trend(average_score, scores):
    """get trend"""
    if average_score < scores[-1]:
        print("The trend is positive")
    else:
        print("The trend is negative")


def get_average_score(scores):
    """get average score"""
    average_score = sum(scores) / len(scores)
    return average_score


def determine_grade(score):
    """get a grade"""
    if score < 50:
        return "N"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    else:
        return "HD"


main()
