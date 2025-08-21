'''Calculate how many numbers are divisible by both 6 and 7 between 1
to 200'''

i = 1
total = 0
while i <= 200:
    if (i % 6 == 0 and i % 7 == 0):
        total = total+1
        print(i, end=' ')
    i = i+1
print("\nTotal numbers divisible by 6 and 7 both :", total)