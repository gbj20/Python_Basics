'''Write a function that takes a list of numbers and prints the sum and
average of these numbers.'''


def Sum_Avg(my_list):
    total = 0
    for i in my_list:
        total += i
    print("Total is:", total)
    avg = total/len(my_list)
    print("Average is:", avg)


Sum_Avg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

