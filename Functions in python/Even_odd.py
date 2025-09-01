'''
Write a function that accepts an integer and prints whether it is odd
or even.
'''


def EvenOdd():
    num = int(input("Enter a Number:"))
    if num % 2 == 0:
        print("Even")
    else:
        print("ODD")


EvenOdd()
