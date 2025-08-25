''' Make your own list. Count the number of even numbers present in
that list.

'''

a = [52, 63, 45, 63, 98, 77, 47, 12, 1, 2, 363, 45, 96]
sum = 0
count = 0
for i in a:
    if (i % 2 == 0):
        count += 1
        sum = sum+i
        print(i, end=' ')
print()
print("count of Even numbers in list is : ", count)
print("sum of Even numbers in list is : ", sum)
