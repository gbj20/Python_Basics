''' Print the following pattern.
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *    '''

# 1. no. of lines i = 5
# 2. no. of columns j = 5

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end=" ")
    print()
