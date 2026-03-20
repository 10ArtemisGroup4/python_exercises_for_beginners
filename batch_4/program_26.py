#display numbers with duplicates
numbers = []
for i in range(10):
    num = int(input(f"Enter the number {i+1}: "))
    numbers.append(num)

seen = set()
duplicates = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    seen.add(num)

print("Numbers with duplicates:", list(duplicates) if duplicates else "No duplicates")