my_dict = {
    "name": "Gayatri",
    "age": 22,
    "gender": "female"
}

print(my_dict)

my_dict.pop("name")
print(my_dict)

my_dict.popitem() #LIFO -- by default pop last item from dict.
print(my_dict)
