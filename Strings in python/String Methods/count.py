'''Ask a string from user. Print the count of how many alphabets, digits,
spaces and symbols (everything else) are there in that string.'''

a = input("Enter any string :")

alpha = 0
digit = 0
space = 0
symbols = 0

for i in a:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        symbols += 1
print(
    f"Alphabets are :{alpha}, Digits are :{digit}, spaces are : {space}, Symbols are:{symbols}")
