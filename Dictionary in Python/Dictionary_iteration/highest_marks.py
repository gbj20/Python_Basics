'''Store name as key, and 5 marks in a list as value in dictionary
store details of at least 5 students. Print the name of the student
who got highest marks'''

student_data = {
    "student1": [85, 90, 78, 92, 88],
    "student2": [75, 88, 92, 80, 87],
    "student3": [90, 95, 89, 78, 93],
    "student4": [80, 85, 88, 92, 87],
    "student5": [92, 88, 95, 90, 85],
}

highest_marks = 0
student_name = ""
for k, v in student_data.items():
    total = sum(v)
    if total > highest_marks:
        highest_marks = total
        student_name = k

print(f"{student_name} : {highest_marks}")
