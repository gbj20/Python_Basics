'''Count the number of spaces in a string entered by user.'''


a = input("Enter any String :")
count = 0
for i in a:
    if i.isspace():
        count += 1
print(count)
