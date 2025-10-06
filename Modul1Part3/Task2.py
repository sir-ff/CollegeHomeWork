number_str = input("Введите четырехзначное число: ")

product = 1

for digit_char in number_str:
    digit = int(digit_char)
    product *= digit

print("Произведение цифр:", product)

