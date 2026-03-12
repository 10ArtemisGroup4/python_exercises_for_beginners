number = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    number.append(num)
for n in number:
    if number.count(n) == 1:
        print (n, end=" ")