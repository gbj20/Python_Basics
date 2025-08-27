'''Start by creating two separate lists with random numbers. Then,
create a third list that merges the numbers from the first and second lists
together.'''

list1 = [10, 52, 30, 56, 45, 78]
list2 = [45, 96, 78, 63, 32]
result = []

for i in list1:
    result.append(i)
for i in list2:
    result.append(i)
print(result)
