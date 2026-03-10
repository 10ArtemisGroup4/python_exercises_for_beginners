odd_numbers = []

for i in range(10):
    try:
        num = int(input(f"Enter number {i+1} of 10: ")) # Get number input and convert to integer
        if num % 2 != 0:
            odd_numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        i -= 1

print("Odd numbers found:", ", ".join(map(str, odd_numbers)))
