a = [50, 20, 63, -52, 45, 96, 78, 96, 32, 42]

print(a)

a.append("Gayu")  # Insert value at the end
a.append(1000)

a.insert(4, 'python')  # insert value at specific index position
a[0] = 100 #update list by index
a.pop(1)  # remove by index
a.remove(96)  # remove by value

print(a)
