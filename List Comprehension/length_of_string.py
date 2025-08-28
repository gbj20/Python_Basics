'''
Given a list of strings, create a new list containing the lengths of
each string using list comprehension
'''

a = ["rose", "apple", "hibiscus", "Lotus", "mango", "banana"]

new_list = [len(a[i]) for i in range(0, len(a))]
print(new_list)
