#BMI = (weight * 703)/height**2

weight = int(input("your weight "))
height = int(input("your height in inches "))

bmi = (weight * 703)/height**2

print("your BMI", bmi)

if bmi>=25:
    print("overweight")
elif bmi<=18.15:
    print("underweight")
else:
    print("you are normal")