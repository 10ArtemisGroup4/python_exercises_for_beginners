#print numbers except ending with 0
for num in range(101):
    if num % 10 == 0:
        continue
    print(num, end=", ")