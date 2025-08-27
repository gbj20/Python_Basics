'''Make a list of your own. And remove all the duplicates element from
that list.'''

a = [10, 10, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30]

duplicates = []

for i in a:
    if i not in duplicates:
        duplicates.append(i)
print(duplicates)
