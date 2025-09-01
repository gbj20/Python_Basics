'''
Create 3 sets of your own, find the union of three sets.
'''

set1 = {1,2,3,45,6}
set2 = {5,6,3,4,8,9}
set3 = {8,9,9,6,2,48,9}

r = set1.union(set2)

r1 = set2.union(set3)

print(r.union(r1))