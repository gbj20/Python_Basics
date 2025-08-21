''' Ask a number from user.
Print “Fizz” if the number is divisible by 3.
Print “Buzz” if the number is divisible by 5.
Print “FizzBuzz” if the number is divisible by 3 and 5.
Print the number itself if none of the conditions are true.

'''

num = int(input("Enter a number :"))


if (num % 3 == 0 and num % 5 == 0):
    print("FIZZBUZZ")
elif (num % 3 == 0):
    print("FIZZ")
elif (num % 5 == 0):
    print("BUZZ")
else:
    print("None of the condition is true for :", num)
