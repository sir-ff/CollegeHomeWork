num1 = int(input("введите число: "))
num2 = int(input("введите число: "))

for num in range(num1,num2+1):
    if num % 7 == 0:
        print(f"кратные 7: {num}")