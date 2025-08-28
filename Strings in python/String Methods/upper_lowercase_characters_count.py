'''Ask a string from user. Count the number of uppercase and
lowercase characters in that String.'''


a = input("Enter any String :")
count1 = 0
count2 = 0
for i in a:
    if i.isupper():
        count1 += 1
print("Uppercase characters are :", count1)
print()
for i in a:
    if i.islower():
        count2 += 1
print("Lowercase characters are :", count2)
