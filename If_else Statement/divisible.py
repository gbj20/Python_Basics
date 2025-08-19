'''Write a program to check if the last digit of a number is divisible by 5
or not.'''

num = input("Enter a number :")
last_digit = num[-1]
print("Last digit is: ", last_digit)
n1 = int(last_digit)
if (n1 % 5 == 0):
    print("Divisible by 5")
else:
    print("Not divisible by 5")
