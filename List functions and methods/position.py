'''
Make a list. Then ask a number from user. If number exists in that list
then print the position of the element else print -1.
'''

a = [52, 63, 45, 89, 74, 32, 45, 63, 96, 78]
num = int(input("Enter a Number :"))


if num in a:
    position = a.index(num)
    print("Position of the number is : ", position)

else:
    print("-1")
