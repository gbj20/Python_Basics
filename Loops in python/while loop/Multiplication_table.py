''' Ask a number from user. Print the multiplication table of that number'''

num = int(input("Enter a Number :"))

i = 1
product = 1
while (i <= 10):
    product = num*i
    print(f"{num}x{i} = {product}")
    i = i+1
