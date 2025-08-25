''' Make your own list. Print the smallest number present in that list'''

a = [52, 63, 45, 63, 98, 77, 47, 12, 1, 2, 363, 45, 96, 30, 10, 20, 0]
# min()
smallest = min(a)
print(smallest)


# for loop
smallest = a[0]

for num in a:
    if num < smallest:
        smallest = num

print("The smallest number is:", smallest)


# sort
a.sort()
smallest = a[0]
print("The smallest number is:", smallest)
