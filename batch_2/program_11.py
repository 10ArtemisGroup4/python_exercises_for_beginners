#smaller number
print("Print the smaller number")
num1, num2 = map(int, input("Put two numbers: ").split())
if num1 < num2:
    print(f"{num1} is smaller")
else:
    print(f"{num2} is smaller")