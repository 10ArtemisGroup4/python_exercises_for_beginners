#sum of 10 numbers
total_sum = 0

for i in range(10):
    # Prompt the user for a number (1-10)
    num = float(input(f"Enter number {i+1}: "))
    total_sum += num

print(f"The sum of all numbers is: {total_sum}")