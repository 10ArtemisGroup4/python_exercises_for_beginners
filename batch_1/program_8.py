count = 0
for _ in range(10):
    if int(input("Enter a number: ")) % 2 != 0:
        count += 1
print("Odd numbers count:", count)