'''Make your own list. Count how many numbers are divisible by both 2
and 5 in that list. '''

a = [52, 63, 45, 63, 98, 77, 47, 12, 1, 2, 363, 45, 96, 30, 10, 20]

count = 0
for i in a:
    if (i % 2 == 0 and i % 5 == 0):
        count += 1
        print(i, end=' ')
print()
print("count of Even numbers in list is : ", count)
