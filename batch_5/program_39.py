#convert to pascal case
full_name = input("Enter a full name (incorrect casing): ")
pascal_case = full_name.title().replace(" ", "")
print(pascal_case)