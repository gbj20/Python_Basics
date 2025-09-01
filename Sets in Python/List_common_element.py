'''
Given two lists a, b. Check if two lists have at least one element
common in them.
'''

a = [1, 2, 3, 45, 69, 78, 15, 25]
b = [1, 5, 45, 6, 9, 8, 7, 63]

a = set(a)
b = set(b)

result = list(a.intersection(b))
print(result)

# print(a & b)