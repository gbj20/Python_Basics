'''
Store marks of 5 different subjects in a dictionary. Ask subject name as an
input from user. Print the marks of that subject entered by user. 
if subject does not exist, print 'Invalid'.
'''

marks = {
    "Physics": 63,
    "chemistry": 85,
    "Maths": 98,
    "History": 89,
}

sub_name = input("Enter Subject Name :")

if sub_name in marks:
    print(marks[sub_name])
else:
    print("Invalid")
