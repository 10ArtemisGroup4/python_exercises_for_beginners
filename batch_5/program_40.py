#convert to snake case
full_name = input("Enter your full name (incorrect casing): ")
snake_case = full_name.title().replace(" ", "_")
print(snake_case)