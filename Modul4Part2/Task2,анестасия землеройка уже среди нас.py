import random

my_karamba = [random.randint(-20, 20) for _ in range(10)]
negative_count = sum(1 for num in my_karamba if num < 0)
Positive_count = sum(1 for num in my_karamba if num > 0)
zero_count = sum(1 for num in my_karamba if num == 0)
print(my_karamba)
print(f"максимальное число: {max(my_karamba)}")
print(f"минимальное число: {min(my_karamba)}")
print(f"кол-во отрицательных чисел: {negative_count}")
print(f"кол-во положительных чисел: {Positive_count}")
print(f"кол-во нулей: {zero_count}")
