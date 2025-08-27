'''Write a program that has two lists and make new list
that contains only the common elements between them
without duplicates.'''

list1 = [10, 20, 30, 40, 50, 50]
list2 = [10, 20, 30, 50, 80, 90, 100]

new_list = []

for i in list1:
    if i in list2:
        if i not in new_list:
            new_list.append(i)
print(new_list)
