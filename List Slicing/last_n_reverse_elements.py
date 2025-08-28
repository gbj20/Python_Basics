'''Ask n from user. Create a list of last n elements but in reverse order
using slicing.

'''

a = [10, 20, 30, 40, 50, 60]

num = int(input("Enter n :"))
for i in a:
    result = a[:-num-1:-1]
print(result)
