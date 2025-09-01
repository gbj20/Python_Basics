'''
Write a function that takes three numbers as parameters and prints
the largest among them.
'''


def largest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print("Largest number is:", num1)
    elif num2 > num1 and num2 > num3:
        print("Largest number is:", num2)
    else:
        print("Largest number is:", num3)


largest(101, 102, 103)
