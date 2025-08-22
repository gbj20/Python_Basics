'''
Enter n = 6

6 6 6 6 6
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1

'''

n = int(input("Enter value for n :"))

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        print(i, end=" ")
    print()
