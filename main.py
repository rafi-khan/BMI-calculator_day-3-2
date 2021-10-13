weight = float(input("Weight: "))
height = float(input("Heaight: "))
BMI = float(round(weight / (height * height)))

if BMI < 18.5:
    print(f"Your BMI is {BMI}, You're underweight")
elif 25 > BMI > 18.5:
    print(f"Your BMI is {BMI}, You've normal weight")
elif 30 > BMI > 25:
    print(f"Your BMI is {BMI}, You're slightly overweight")
elif 35 > BMI > 30:
    print(f"Your BMI is {BMI}, You're obese")
else:
    print(f"Your BMI is {BMI}, You're clinically obese") 