my_dict = {
    "name": "Gayatri",
    "age": 22,
    "gender": "female"
}

print(my_dict)

# Method 1
my_dict["age"] = 25
print(my_dict)

# Method 2
my_dict.update({"marks": 99, "address": "Delhi"})
print(my_dict)
