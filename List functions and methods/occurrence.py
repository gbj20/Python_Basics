'''Write a python code to find the occurrence of each element in a list and
print the element with the highest occurrence.'''

a = [10, 10, 10, 20, 20, 30, 30, 40, 50, 60, 2, 2, 2, 2, 2]
duplicates = []
for i in a:
    if i not in duplicates:
        duplicates.append(i)
# print(duplicates)

# highest occurrence element

highest_occur_element = 0
highest_occurence = 0


for i in duplicates:
    result = a.count(i)
    print(f"{i} occurs {result} times")
    if result > highest_occurence:
        highest_occurence = result
        highest_occur_element = i


print(f"Highest occurence element: {highest_occur_element}")
