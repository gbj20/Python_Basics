'''Write a program that converts a string in camelCase to snake_case.
For example, converting "helloWorldHowAreYou" should result in
"hello_world_how_are_you".'''


camel_str = "helloWorldHowAreYou"
snake_str = ""

for char in camel_str:
    if char.isupper():
        snake_str += "_" + char.lower()
    else:
        snake_str += char

print(snake_str)
