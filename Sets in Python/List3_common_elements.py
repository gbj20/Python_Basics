'''
Python program to find common elements in three lists using sets.
'''

a = [1, 2, 3, 45, 63, 78, 15, 25]
b = [1, 5, 45, 6, 9, 8, 7, 63]
c = [1, 56, 63, 78, 45]

a = set(a)
b = set(b)
c = set(c)

result = a.intersection(b)
result1 = result.intersection(c)
print(result1)

# print(a & b & c)
