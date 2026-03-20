#replicate removeprefic()
user_input = input("enter text: ")
prefix = input("enter prefix to remove: ")
if user_input.startswith(prefix):
    result = user_input[len(prefix):]
else:
    result = user_input
print(result)