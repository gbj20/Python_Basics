# # Add two numbers and take input from user

num1 = int(input("Enter first number :"))
num2 = int(input("Enter Second number :"))
print("sum is :", num1+num2)

# # type conversion

x = 123
y = "1809"
a = int(y)
b = str(x)
print(type(a))
print(type(b))


# # area of rectangle
length = int(input("Enter value for length :"))
width = int(input("Enter value for width :"))
area_of_rectangle = length*width
print(area_of_rectangle)


# Average of three numbers

num1 = int(input("Enter first number :"))
num2 = int(input("Enter Second number :"))
num3 = int(input("Enter third number :"))

result = (num1+num2+num3)/3
print(result)

# convert float to an integer and vice versa

x = 45
y = 55.55

a = int(y)
b = float(x)

print(a)
print(b)

'''Write a program that converts a temperature in Fahrenheit to Celsius.
The formula is: Celsius = (Fahrenheit - 32) * 5/9.'''

temperature = 23

celsius = ((temperature-32)*5)/9
print(celsius)
