a = "Hello World"
# split

words = a.split()
print(words)

print(len(words))

# join
a = ["Hello", "world"]

my_string = "_".join(a)
print(my_string)


# comprehension

a = ["Hello", "world"]

my_string = " ".join(str(i)[::-1] for i in a)
print(my_string)
