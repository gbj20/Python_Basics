''' Calculate factorial of a number entered by user.
Example:
Enter a number = 5
Factorial of a number means product of all the numbers from 1 to that
number.
5 factorial = 5 x 4 x 3 x 2 x 1
Output = 120
'''
num = int(input("Enter a Number :"))
fact = 1
i = 1
while (i < num):
    fact = num*fact
    num = num-1
i = i+1
print(fact)
