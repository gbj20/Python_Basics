'''
Convert two lists into a dictionary. Make two lists
on you own of same length, and convert them to dictionary.
'''

list1 = ['Ten', 'Twenty', 'Thirty']
list2 = [10, 20, 30]

my_dict = {}

for i in range(0,len(list1)):
    my_dict[list1[i]] = list2[i]
print(my_dict)
