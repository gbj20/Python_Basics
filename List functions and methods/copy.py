'''Take 10 integer inputs from user and store them in a list. Now, copy
all the elements in another list but in reverse order.

'''
list_length = int(input("Enter Length of list: "))
list1 = []

for i in range(0, list_length):
    num = int(input("Enter a number :"))
    list1.append(num)
print(list1)

# result = list1.copy()
# result.reverse()
# print(result)

#another way instead of using .copy() and .reverse()
result = []
for i in range(len(list1)-1, -1, -1):
    result.append(list1[i])
print(result)
