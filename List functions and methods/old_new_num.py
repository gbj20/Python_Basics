'''105'''

a = [52, 63, 45, 89, 74, 32, 45, 63, 96, 78]
old_num = int(input("Enter old Number:"))
new_num = int(input("Enter New Number :"))

for i in range(0, len(a)):
    if old_num == a[i]:
        a[i] = new_num
print(a)
