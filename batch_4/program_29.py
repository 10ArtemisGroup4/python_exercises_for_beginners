#highest to lowest
numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
if numbers:
    numbers.sort(reverse=True)
    print("Numbers from highest to lowest:", numbers)
else:
    print("No valid numbers found")