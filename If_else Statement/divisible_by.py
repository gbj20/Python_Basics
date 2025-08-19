'''Write a program that takes two numbers as input and checks if the
first number is divisible by the second'''

num1 = int(input("Enter a number1 :"))
num2 = int(input("Enter a number2 :"))

if num1 % num2 == 0:
    print("num1 is divisible by num2")
else:
    print("num1 is not divisible by num2")
