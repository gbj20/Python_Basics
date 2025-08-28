'''Ask a string from user. Count how many alphabets are there in that
string.'''

a = input("Enter any string :")
count = 0
for i in a:
    if a.isalpha():
        count += 1
print(count)
