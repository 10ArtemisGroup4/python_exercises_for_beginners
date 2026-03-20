#display the highest number
max_num = None
while True:
    try:
        num = int(input("Enter a number: "))
        if max_num is None or num > max_num:
            max_num = num
    except ValueError:
        break
if max_num is not None:
    print(f"The highest number is {max_num}")
else:
    print("No valid numbers found")