my_string = "Gayatri Jadhav"

# By index

for i in range(0, len(my_string)):
    print(my_string[i], end=' ')

print()

# By value

for i in my_string:
    print(i, end=' ')

print()

# reverse string

for i in range(len(my_string)-1, -1, -1):
    print(my_string[i], end=" ")
