'''Write a program to split a given list into two halves.'''

a = [10, 20, 30, 40, 50, 60, 70]
mid = len(a) // 2
x = []
y = []

for i in range(mid):
    x.append(a[i])

for i in range(mid, len(a)):
    y.append(a[i])

print(x)
print(y)
