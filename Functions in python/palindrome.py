'''Write a function that takes a string and prints whether it is a
palindrome.'''


def palindrome():
    my_string = input("Enter a string :")
    result = my_string[::-1]
    if result == my_string:
        print("Given String is a Palindrome!!")

    else:
        print("Given String is not a Palindrome!!")


palindrome()
