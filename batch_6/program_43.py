#replicate lower()
user_input = input("Enter text: ")
result = ""
for char in user_input:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    else:
        result += char
print(result)