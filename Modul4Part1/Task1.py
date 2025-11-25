print("Задание 1: Проверка на палиндром")
text = input("Введите строку: ")

text_clean = text.replace(" ", "").lower()

text_reverse = ""
for i in range(len(text_clean)-1, -1, -1):
    text_reverse += text_clean[i]

if text_clean == text_reverse:
    print("это палиндром")
else:
    print("это не палиндром")