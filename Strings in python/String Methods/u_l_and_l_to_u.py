''' Ask a string from user. Convert uppercase to lowercase and convert
lowercase to uppercase and don’t change the other letters.'''

#Method 1


a = input("Enter any String :")
b = a.swapcase()
print(b)


#Method 2

# for i in a:
#     if i.upper():
#         result = i.lower()
#     print(result, end=' ')

# print()

# for i in a:
#     if i.lower():
#         result = i.upper()
#     print(result, end=' ')
