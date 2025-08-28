'''
Write a program that accepts a string and capitalizes the first letter
of each word while converting all other letters to lowercase.
'''
words = "gayatri jadhav"
words = words.split()

words = " ".join(i.title() for i in words)
print(words)
