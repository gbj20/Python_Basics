my_dict = {
    "name": "Gayatri",
    "age": 22,
    "gender": "female"
}
print(my_dict)

# print(my_dict.keys())

for k in my_dict.keys():  # Print keys
    print(k)


for k in my_dict.values():  # Print values
    print(k)


my_dict = {
    "science" : 89,
    "Maths" : 98,
    "Comp" : 93
}

total = 0
for v in my_dict.values():
    total+=v

print(total)