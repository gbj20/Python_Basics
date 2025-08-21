'''Write a program that calculates a person's BMI based on their height
(in meters) and weight (in kilograms). Use the following formula: BMI =
weight / (height^2). Then, classify the BMI according to the following
ranges:
Underweight: BMI less than 18.5
Normal weight: BMI 18.5 - 24.9
Overweight: BMI 25 - 29.9
Obesity: BMI 30 or greater'''



weight = float(input("Enter person's weight (in kg): "))
height = float(input("Enter person's height (in meters): "))

BMI = weight / (height ** 2)
print("BMI:", BMI)

if BMI < 18.5:
    print("Underweight")
else:
    if BMI <= 24.9:
        print("Normal weight")
    else:
        if BMI <= 29.9:
            print("Overweight")
        else:
            print("Obesity")
