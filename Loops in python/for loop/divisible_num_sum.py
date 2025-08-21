'''Write a program to calculate the sum of all the numbers divisible by 4
from 20 to 50'''
count = 0
for i in range(20, 51):
    if (i % 4 == 0):
        count = count+1
        print(i, end=' ')
print("\nTotal numbers divisible by 7 for 1 to 100 are :", count)
