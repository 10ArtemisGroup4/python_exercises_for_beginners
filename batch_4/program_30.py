#display the average
total = 0
count = 0

while True:
    try:
        num = float(input("Enter a number: "))
        total += num
        count += 1
    except ValueError:
        break
if count > 0:
    average = total / count
    print(f"The average is {average:.2f}")
else:
    print("No valid numbers found")