"""
 function main
    human_year = float(input("please enter your dog's human age :"))
    while human_year > 0 :
          dog_year(human_year)
          human_year = float(input("please enter your dog's human age :"))
    print("bye")
"""

def main():
    """to know the different age between human and dog."""
    human_year = float(input("please enter your dog's human age :"))
    while human_year > 0 :
          dog_year(human_year)
          human_year = float(input("please enter your dog's human age :"))
    print("bye")

def dog_year(human_year):
    """get doy age."""
    if human_year <= 2 :
       dog_year = human_year * 10.5
    else:
        dog_year = (human_year - 2) * 4 + (10.5 * 2)
    print(dog_year)

main()