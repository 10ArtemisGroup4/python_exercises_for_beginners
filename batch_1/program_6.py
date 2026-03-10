#first number is raised by the second number
print("First number is raised to the Second number")
num1, num2, = map(int,input("Put two number: ").split())
power = num1 ** num2
print(f"{num1} raised to {num2} is {power}")
