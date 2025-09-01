'''
Ask a string from user, remove all the duplicates from that string and
print that string again (order does’nt matter)

'''

my_string = input("Enter any String: ")

result = set(my_string)
print(result)

final_result = "".join(result)
print(final_result)
