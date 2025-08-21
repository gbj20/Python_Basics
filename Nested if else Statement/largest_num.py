'''Write a program that takes three numbers as input and determines
the largest one using nested if-else statements. Make sure all 3 numbers
entered by user are different'''

num1 = int(input("Enter First Number :"))
num2 = int(input("Enter Second Number :"))
num3 = int(input("Enter Third Number :"))

if(num1>num2):
    if(num1>=num2):
        print(f"{num1} is Largest!!")
    else:
        print(f"{num2} is Largest")
else:
    if(num2>num3):
        print(f"{num2} is Largest!!")
    else:
        print(f"{num3} is Largest!!")
        