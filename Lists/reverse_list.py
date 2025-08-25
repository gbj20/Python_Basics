a = [12, 34, 56, 44, 67, 12.2, 2, 4, 5, 7, 3, 9]
x = a[:: -1]
print(x)


# find even numbers present in the list
for i in a:
    if (i % 2 == 0):
        print(i)


for i in a:
    if (i % 2 != 0):
        print(i, end=" ")
