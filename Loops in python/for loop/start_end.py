''' Ask start number and end number from user. Print all the numbers
from start to end using while loop.'''

start_num = int(input("Enter start Number :"))
end_num = int(input("Enter end number :"))

for i in range(start_num, end_num+1):
    print(i, end = " ")