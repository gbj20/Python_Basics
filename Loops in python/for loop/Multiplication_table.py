'''Ask a number from user. Print the multiplication table of that number.'''
num = int(input("Enter a Number :"))
product = 1
for i in range(1, 11):
    product = num*i
    print(f"{num}x{i} = {product}")
