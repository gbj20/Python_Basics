'''
Write a python program to combine two dictionary by 
adding value for common key.

'''

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = {}

for k, v in d1.items():
    result[k] = v

for k, v in d2.items():
    if k in result:
        result[k] = result[k]+v
    else:
        result[k] = v
print(result)




