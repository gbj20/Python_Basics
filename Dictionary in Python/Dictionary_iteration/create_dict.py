''' 
Ask subject name and marks from the user and keep adding it to
dictionary
'''
my_dict = {}
total = int(input("Enter total no. of subjects :"))

for i in range(0, total):
    k = input("Enter subject name :")
    v = int(input("Enter marks of subject :"))
    my_dict[k]=v
print(my_dict)
