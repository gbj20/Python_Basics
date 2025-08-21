'''Calculate how many numbers are divisible by 7 from 1 to 100.'''

i = 1
total = 0
while i <= 100:
    if (i % 7 == 0):
        total += 1
        print(i, end=' ')
    i = i+1
print("\nTotal Numbers divisible by 7 : ", total)
