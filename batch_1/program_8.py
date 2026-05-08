count = 0
for i in range(10):
    if int(input(f"Enter a number {i+1}: ")) % 2 != 0:
        count += 1
print("Odd numbers count:", count)