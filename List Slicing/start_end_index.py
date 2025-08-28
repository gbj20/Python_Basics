'''Ask start and end index from the user. Create a list from start index
to end index using slicing.
'''

a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

start_index = int(input("Enter a start index :"))
end_index = int(input("Enter a end index :"))

for i in a:
    result = a[start_index:end_index+1]
print(result)
