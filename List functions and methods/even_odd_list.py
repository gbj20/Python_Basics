''' Generate a list of at least 10 numbers. Then, create two separate
lists called 'odd' and 'even.' Put all the odd numbers from the original list
into the 'odd' list, and all the even numbers into the 'even' list.
'''
a = [52, 63, 45, 89, 74, 32, 45, 63, 96, 78, 1, 2, 5, 7]

odd_list = []
even_list = []

# for i in range(0, len(a)): #iterate by index
#     if a[i] % 2 == 0:
#         even_list.append(a[i])
#     else:
#         odd_list.append(a[i])
# print("Even list elements are :",even_list)
# print("Odd list elements are :",odd_list)

for i in a:  #iterate by value
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Even list elements are :",even_list)
print("Odd list elements are :",odd_list)
