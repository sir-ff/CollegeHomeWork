num1 = int(input("введите число: "))
num2 = int(input("введите число: "))

summa = 0

for num in range(num1, num2 + 1):
    if num % 9 == 0:
        summa += num
        print(f"Сумма четных чисел от 0 до {num} равна = {summa}")
for num in range(num1, num2 + 1):
    if num % 9 != 0:
        summa += num
        print(f"Сумма нечетных числел то 0 до {num} = {summa}")