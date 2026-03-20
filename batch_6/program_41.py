#replicate lstrip()
index = 0
user_input = input("enter text with spaces in front: ")
while index < len(user_input) and user_input[index] == " ":
    index += 1
result = user_input[index:]
print(result)