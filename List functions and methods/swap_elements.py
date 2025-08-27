'''Write a program that swaps the first and last elements of a given list'''

a = [10, 20, 30, 40, 50]


a[0], a[-1] = a[-1], a[0]
print("List after swapping first and last elements:", a)
