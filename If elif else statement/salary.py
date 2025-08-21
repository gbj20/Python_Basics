'''Take Salary as input from User and Update the salary of an employee.
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment

'''

salary = int(input("Enter Final salary:"))

if (salary < 10000):
    salary = (salary*5)/100 + salary
    print("You got 5% increment!!", "\nYour final salary is", salary)
elif (salary >= 10000 and salary <= 20000):
    salary = (salary*10)/100 + salary
    print("You got 10% increment!!", "\nYour final salary is", salary)
elif (salary >= 20000 and salary <= 50000):
    salary = (salary*15)/100 + salary
    print("You got 15% increment!!", "\nYour final salary is", salary)
elif (salary > 50000):
    salary = (salary*20)/100 + salary
    print("You got 20% increment!!", "\nYour final salary is", salary)
else:
    print("No increment for", salary)