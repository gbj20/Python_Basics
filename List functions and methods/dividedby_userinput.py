'''107'''

num = int(input("Enter a Number :"))
a = [52, 97, 63, 45, 89, 74, 32, 45, 63, 96, 78, 2, 10, 12, 16, 3]
result = []

for i in range(0, len(a)):
    if a[i] % num == 0:
        result.append(a[i])
print(result)
