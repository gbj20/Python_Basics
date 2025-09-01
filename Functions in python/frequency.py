'''Write a function that accepts a string and prints the frequency of
each character in the string.'''


def char_frequency():
    my_dict = {}
    my_string = input("Enter any String :")

    for i in my_string:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    print(my_dict)

    for k, v in my_dict.items():
        print(f"{k} occurs {v} times!!")


char_frequency()
