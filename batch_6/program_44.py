#replicate isupper()
user_input = input("enter text: ")
is_all_upper = True
has_letter = False

for char in user_input:
    if char.isalpha():
        has_letter = True
        if not ('A' <= char <= 'Z'):
            is_all_upper = False
            break
print(is_all_upper and has_letter)