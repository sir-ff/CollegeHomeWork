summa = 0
count = 0
max_num = float('-inf')
min_num = float('inf')

while True:
    num = int(input('для завершения введите 7\nвведите число: '))
    if num == 7:
        print("Good bye")
        break
    summa += num
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
    count += 1
print(f'Summa: {summa}')
print(f'max_num: {max_num}')
print(f'min_num: {min_num}')