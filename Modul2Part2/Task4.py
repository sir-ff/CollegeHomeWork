num1 = int(input('в ведите число: '))
num2 = int(input('в ведите число: '))

if num1 == num2:
    print('равны')
elif num1 != num2:
    sorted_num = sorted([num1, num2])
    print(sorted_num)
else:
    print('error')