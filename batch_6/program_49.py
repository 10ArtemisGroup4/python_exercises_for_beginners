#Replicate capitalize() without using the function
user_input = input("Enter text: ")
if not user_input:
    print("")
else:
    # First character uppercase, rest lowercase
    first_char = chr(ord(user_input[0]) - 32) if 'a' <= user_input[0] <= 'z' else user_input[0]
    rest = ""
    for char in user_input[1:]:
        if 'A' <= char <= 'Z':
            rest += chr(ord(char) + 32)
        else:
            rest += char
    print(first_char + rest)