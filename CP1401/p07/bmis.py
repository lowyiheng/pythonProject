HEIGHT = 1.75
def main():
    for weight in range (50 ,100 +1 ,2):
        bmi = calculate_bmi(HEIGHT, weight)
        category = determine_weight_category(bmi)
        print(f"Height {HEIGHT}m, Weight {weight}kg = BMI {calculate_bmi(HEIGHT, weight):.1f} , considered {category} ")

def calculate_bmi(HEIGHT, weight):
    bmi = weight / (HEIGHT ** 2)
    return bmi

def determine_weight_category(bmi):
  if bmi < 18.5:
    return "underweight"
  elif bmi < 25:
    return "normal"
  elif bmi < 30:
    return "overweight"
  else:
    return "obese"

# main()

def main():
    for height in range (150 ,191 ,10):
        for weight in range (50 ,100 +1 ,10):
            meter = centimetre_to_meter(height)
            bmi = calculate_bmi(meter, weight)
            category = determine_weight_category(bmi)
            print(f"Height {meter}m, Weight {weight}kg = BMI {calculate_bmi(meter, weight):.1f} , considered {category}")

def calculate_bmi(meter, weight):
    bmi = weight / (meter ** 2)
    return bmi

def determine_weight_category(bmi):
  if bmi < 18.5:
    return "underweight"
  elif bmi < 25:
    return "normal"
  elif bmi < 30:
    return "overweight"
  else:
    return "obese"

def centimetre_to_meter(height):
    meter = height / 100
    return meter

main()