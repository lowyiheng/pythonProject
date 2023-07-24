def main():
  height = get_valid_number("enter height :" ,0 ,3)
  weight = get_valid_number("enter weight(kg):" ,0 ,300)
  bmi = calculate_bmi(height, weight)
  category = determine_weight_category(bmi)
  print(f"This BMI is {bmi}, which is considered {category}")

def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number

def calculate_bmi(height, weight):
    return weight / (height ** 2)

def determine_weight_category(bmi):
  if bmi < 18.5:
    return "underweight"
  elif bmi < 25:
    return "normal"
  elif bmi < 30:
    return "overweight"
  else:
    return "obese"

# def test_determine_weight_category():
#     print(determine_weight_category(18.4))
#     print(determine_weight_category(31))
#     print(determine_weight_category(26.6))
#     print(determine_weight_category(28.8))
#     print(determine_weight_category(18.5))
# test_determine_weight_category()
#
# def test_calculate_bmi():
#     print(calculate_bmi(1.6 ,58))
#     print(calculate_bmi(2 ,60))
#     print(calculate_bmi(5 ,100))
# test_calculate_bmi()

main()

