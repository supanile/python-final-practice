def get_bmi(height, weight):
    bmi = weight / ((height / 100) ** 2)

    if bmi < 18:
        print("Underweight")
    elif 18.5 <= bmi <= 22.9:
        print("Slim")
    elif 23 <= bmi <= 24.9:
        print("Overweight")
    elif 25 <= bmi <= 29.9:
        print("Fat")
    else:
        print("Dangerous obesity")

height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

get_bmi(height, weight)
