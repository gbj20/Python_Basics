'''
Store "name" of a student as key. "list of 5 marks" of that students as a value.
store atleast 5 student names. print the sum and percentage of all the students.

'''

student_data = {
    "student1": [85, 90, 78, 92, 88],
    "student2": [75, 88, 92, 80, 87],
    "student3": [90, 95, 89, 78, 93],
    "student4": [80, 85, 88, 92, 87],
    "student5": [92, 88, 95, 90, 85],
}

for k, v in student_data.items():
    total = sum(v)
    percentage = total/500*100
    print(f"{k} scored total {total} marks, percentage={percentage:.2f}")
