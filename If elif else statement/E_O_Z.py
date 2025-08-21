'''Write a program to check if the number is ODD, EVEN or Equal to Zero.'''
num = int(input("Enter a number :"))

if (num % 2 == 0):
    print("Even")
elif (num == 0):
    print("It is equal to zero")
else:
    print("Odd")
