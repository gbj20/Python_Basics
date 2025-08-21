'''Ask start number and end number from user. Print all the numbers
from start to end using while loop.
'''

start_num = int(input("Enter start Number :"))
end_num = int(input("Enter end number :"))

i = start_num
while i <= end_num:
    print(i, end=' ')
    i = i+1
