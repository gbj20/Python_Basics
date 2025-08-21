'''Calculate how many numbers are divisible by both 6 and 7 between 1
to 200.'''

count = 0
for i in range(2,201):
    if(i%6==0 and i%7==0):
        count = count+1
        print(i, end=" ")
print("\nTotal numbers divisible by 7 for 1 to 100 are :", count)