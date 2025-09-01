'''
Write a function that takes an integer and prints whether it is a
prime number
'''


def prime():
    num = int(input("Enter a Number:"))
    factors = 0
    for i in range(1, num+1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        print("It's Prime!!")
    else:
        print("Not Prime!!")


prime()
