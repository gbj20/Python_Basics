'''A student will not be allowed to sit in exam if his/her attendance is
less than 75%.
Take following input from user:
Number of classes held
Number of classes attended.
1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not.'''



'''Attendance Percentage=(Classes Attended/Total Classes Held)×100'''


no_of_classes_held = int(input("Enter total classes held :"))
no_of_classes_attended = int(input("Enter Number of classes attended :"))

percentage_of_class_attended = (no_of_classes_attended / no_of_classes_held)*100
print("percentage of class attended", percentage_of_class_attended)

if (percentage_of_class_attended < 75):
    print("Student is not allowed to sit in exam!!")
else:
    print("Student is allowd to sit in a exam!!")
