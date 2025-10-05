num1 = float(input())
num2 = float(input())
num3 = float(input())

choice = input().lower()

if choice == "sum":
    result = num1 + num2 + num3
    print(f"sum: {result}")
elif choice == "product":
    result = num1 * num2 * num3
    print(f"product: {result}")
else:
    print("error")