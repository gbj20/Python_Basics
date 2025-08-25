'''Make your own list. Print the largest number present in that list.'''

a = [52, 63, 45, 63, 98, 77, 47, 12, 1, 2, 363, 45, 96, 30, 10, 20]

reversed = max(a)
print(reversed)

# using for loop
largest = a[0]

for num in a:
    if num > largest:
        largest = num

print("The largest number is:", largest)


# sort
a.sort()
largest = a[-1]
print("The largest number is:", largest)
