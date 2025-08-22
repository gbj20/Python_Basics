'''
Ask N from user. N means number of lines. print the following patter.
Enter n = 8

1 1 1 1 1
2 2 2 2 2 
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5 
6 6 6 6 6
7 7 7 7 7
8 8 8 8 8

'''
n = int(input("Enter value for n :"))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(i, end=" ")
    print()
