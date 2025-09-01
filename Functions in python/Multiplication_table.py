'''
Write a function that accepts an integer and prints the
multiplication table for that number up to 10
'''


def table():
    num = int(input("Enter a Number:"))
    product = 1
    for i in range(1, 11):
        product = num*i
        print(f"{num}X{i} = {product}")


table()
