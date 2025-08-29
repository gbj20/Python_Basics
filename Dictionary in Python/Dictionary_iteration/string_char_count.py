'''
Ask a string from user. Display the dictionary where each key is a
character and value is the frequency of that character that comes in
that string.

'''

my_string = input('Enter any string :')
my_dict = {}
for i in my_string:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print(my_dict)
