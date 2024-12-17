"""BIM(body mass index) is a tool taht healthcare providers use to estimate the amount of body
fat by using your height and weight measurements"""

weight=float(input("enter your weight:"))
height=float(input("enter your height:"))
bmi=round(weight/height)**2
if bmi<18.5:
    print(f"you are IBM {bmi} and you are underweight.")
elif bmi<25:
    print(f"you are IBM {bmi} and you are a normal weight.")
elif bmi<30:
    print(f"you are BMI {bmi} and you are overweight.")
elif bmi<35:
    print(f"you are IBM {bmi} and you are obese.")
else:
    print(f" you are IBM {bmi} and you are clinically obese")