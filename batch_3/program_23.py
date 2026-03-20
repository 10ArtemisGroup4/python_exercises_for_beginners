#finding the duplicate and unique
nums = []
duplicates = {}
while True:
    try:
        num = float(input("Enter number: "))
        nums.append(num)
        if num not in duplicates:
            duplicates[num] = 1
            print("Unique")
        else:
            duplicates[num] = duplicates[num] + 1
            print("Duplicate")
    except ValueError:
        break