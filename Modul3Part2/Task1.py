num1 = int(input("введите число: "))
num2 = int(input("введите число: "))

summa = 0
count = 0

for num in range(num1, num2 + 1):
    if num % 2 == 0:
        summa += num
        count += 1
        print(f"Сумма четных чисел = {summa}","арефмитическое =", summa // count)
    if num % 2 != 0:
        summa += num
        count += 1
        print(f"Сумма нечетных числел = {summa}","арефмитическое =", summa // count)
    if num % 9 ==0:
        summa += num
        count += 1
        print(f"сумма четных числел 9 = {summa}","арефмитическое =", summa // count)
