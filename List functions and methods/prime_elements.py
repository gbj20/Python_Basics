'''Write a program to find and print all prime numbers within a given list.'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 19]

factors = 0

for num in a:
    factors = 0
    for i in range(1, num+1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        print(num, end=' ')
