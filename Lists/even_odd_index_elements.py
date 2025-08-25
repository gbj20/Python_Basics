'''Make your own list. Print all the elements present at even and odd index
position.

'''

a = [52, 63, 45, 63, 98, 77, 47, 12, 1, 2, 363, 45, 96]
b = len(a)

for i in range(0, b):
    if (a[i] % 2 == 0):
        print(a[i], end=' ')
print()

for i in range(0, b):
    if (a[i] % 2 != 0):
        print(a[i], end=' ')
