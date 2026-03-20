#replicate endswith()
user_input = input("Enter text: ")
suffix = input("Enter suffix to check: ")
if len(suffix) > len(user_input):
    print(False)
else:
    print(user_input[-len(suffix):] == suffix)