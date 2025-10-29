num = input("Введите целое число: ")

new_num_str = ""
for digit in num:
  if digit != '3' and digit != '6':
    new_num_str += digit

# 3. Вывести результат
print("Число без цифр 3 и 6:", new_num_str)

