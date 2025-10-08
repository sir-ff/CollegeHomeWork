num1 = int(input("введите число: "))
num2 = int(input("введите число: "))

for num in range(num1,num2+1):
    print(f"все числа диапозона: {num}")

sort = sorted([num for num in range(num1,num2+1)], reverse=True)
print(f"в убывающем порядке: {sort}")

for num in range(num1,num2+1):
    if num % 7 == 0:
        print(f"кратные 7: {num}")
for num in range(num1,num2+1):
    if num % 5 == 0:
        print(f"кратные 5: {num}")