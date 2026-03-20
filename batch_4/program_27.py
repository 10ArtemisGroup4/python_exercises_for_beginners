#display the numbers eith most duplicates
counts = {}
while True:
    try:
        num = int(input("Enter a number: "))
        counts[num] = counts.get(num, 0) + 1
    except ValueError:
        break

if counts:
    max_count = max(counts.values())
    most_duplicates = [num for num, cnt in counts.items() if cnt == max_count]
    print(f"Most duplicates ({max_count} times): {most_duplicates}")
else:
    print("No numbers found")