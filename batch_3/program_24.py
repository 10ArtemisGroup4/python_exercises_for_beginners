#lowest to highest
nums = []
while True:
    try:
        num = float(input("Enter number: "))
        nums.append(num)
    except ValueError:
        break
print(f"The lowest number is: {min(nums)}")