'''
Remove all the even numbers from the list
'''

# a = [52, 63, 45, 89, 74, 32, 45, 63, 96, 78, 2, 10, 12, 16, 3]
# result = []

# for i in range(0, len(a)):
#     if a[i] % 2 != 0:
#         result.append(a[i])
# print(result)

a = [45,66,66,66,66,78,11,11,12,12,12]

for i in range(0, len(a)):
    if a[i] % 2 != 0:
        print(a[i], end=' ')
