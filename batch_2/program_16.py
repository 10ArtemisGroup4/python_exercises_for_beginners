#10 numbers then the first number - all the remaining
number = []

for i in range(10):
    num = float(input(f"Enter a number {i+1}: "))
    number.append(num)

result = number[0]

for i in range(1, 10):
    result -= number[i]

print(f"Result is {result}")
