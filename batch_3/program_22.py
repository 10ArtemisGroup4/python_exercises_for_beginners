numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

for n in numbers:
    if n not in numbers[:numbers.index(n)]:
        print(n)