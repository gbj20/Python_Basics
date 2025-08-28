'''Write a program to reverse the order of words'''

my_string = "Python is good"

result = my_string.split()
# print(result)
result = result[::-1]
# print(result)
result2 = " ".join(result)
print(result2)
