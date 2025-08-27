'''Write a python code to find the second largest element
in a list without sorting.'''

a = [52, 63, 45, 89, 74, 32, 45, 63, 96, 78]

largest = float("-inf")
second_largest = float("-inf")
for i in a:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i < largest:
        second_largest = i
print(second_largest)

