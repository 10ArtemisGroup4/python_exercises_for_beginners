#print the bigger number
print("Check the Bigger Number")
num1, num2 = map(int, input("Put two numbers: ").split())
if num1 > num2:
    print(f"{num1} is bigger")
else:
    print(f"{num2} is bigger")