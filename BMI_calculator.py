weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(meters): "))

bmi = weight/(height**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f} and you are in underweight")
elif 18.5 >= bmi < 25 :
    print(f"Your BMI is {bmi:.2f} and you are in normal weight")
elif 25 >= bmi < 30:
    print(f"Your BMI is {bmi:.2f} and you are in overweight")
else:
    print(f"Your BMI is {bmi:.2f} and you are in obese")