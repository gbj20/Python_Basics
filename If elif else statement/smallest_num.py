'''Ask 4 numbers from user. Make sure all the numbers entered by user
are different. Print which number is the smallest.'''

num1 = (input("Enter first number : "))
num2 = (input("Enter second number : "))
num3 = int(input("Enter third number : "))
num4 = int(input("Enter fourth number : "))


if (num1 < num2 and num1 < num3 and num1 < num4):
    print(num1, "is smallest")
elif (num2 < num1 and num2 < num3 and num2 < num4):
    print(num2, "is smallest")
elif (num3 < num2 and num3 < num1 and num3 < num4):
    print(num3, "is smallest")
else:
    print(num4, "is smallest")
