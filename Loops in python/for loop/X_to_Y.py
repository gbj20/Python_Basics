'''Ask to numbers x and y from the user. If x<y then print all the
numbers from x to y, but if y<x then print all the numbers from y to x.'''


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x < y:
    for i in range(x, y + 1):
        print(i, end=" ")
elif x > y:
    for i in range(x, y - 1, -1):  
        print(i, end=" ")
else:
    print(x)  
