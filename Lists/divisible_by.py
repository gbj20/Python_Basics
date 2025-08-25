'''Make your own list. Find the sum of all numbers divisible by 3 or 4.
'''

a = [52, 63, 45, 63, 98, 77, 47, 12, 1, 2, 363, 45, 96, 30, 10, 20]
sum = 0
count = 0
for i in a:
    if (i % 3 == 0 or i % 4 == 0):
        count += 1
        sum = sum+i
        print(i, end=' ')
print()
print("count of numbers divisible by 3 or 4 in list is : ", count)
print("sum of numbers divisible by 3 or 4 in list is : ", sum)
