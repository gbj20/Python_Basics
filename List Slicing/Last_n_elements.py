''' Implement a python program to get the last 'n' elements from a list
using slicing'''

a = [10, 20, 30, 40, 50, 60]

num = int(input("Enter n :"))
for i in a:
    result = a[-num:]
print(result)
