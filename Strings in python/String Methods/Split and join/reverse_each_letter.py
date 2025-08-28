'''
Write a program that reverses each word in a sentence while
maintaining the word order. For example, "Hello World" should become
"olleH dlroW".
'''


a = "Hello world"
a = a.split()

my_string = " ".join(str(i)[::-1] for i in a)
print(my_string)