'''
Write a python program to multiply all the items in a dictionary
'''

marks = {
    "Physics": 63,
    "chemistry": 85,
    "Maths": 98,
    "History": 89,
}

total = 1

for v in marks.values():
    total *= v
print(total)
