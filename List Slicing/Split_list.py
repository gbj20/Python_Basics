'''Implement a python program to split a list into two equal parts using
slicing. One list should contain 1st half and another list should contain 2nd
half.'''
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

list1 = a[:len(a)//2]
list2 = a[len(a)//2:]

print(list1)
print(list2)
