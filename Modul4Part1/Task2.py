text = input("Введите текст: ")
words_input = input("Введите зарезервированные слова через пробел: ")

# Разбиваем на слова
reserved_words = words_input.split()

# Разбиваем текст на слова
text_words = text.split()

# Новый список для результата
new_text_words = []

# Проверяем каждое слово
for word in text_words:
    # Убираем знаки препинания вокруг слова
    word_clean = word
    if len(word) > 0:
        # Проверяем первый и последний символ
        first_char = ''
        last_char = ''

        if word[0] in '.,!?;:':
            first_char = word[0]
            word_clean = word[1:]

        if word_clean and word_clean[-1] in '.,!?;:':
            last_char = word_clean[-1]
            word_clean = word_clean[:-1]

        # Проверяем, есть ли слово в списке
        found = False
        for reserved in reserved_words:
            if word_clean.lower() == reserved.lower():
                new_word = first_char + word_clean.upper() + last_char
                new_text_words.append(new_word)
                found = True
                break

        if not found:
            new_text_words.append(word)
    else:
        new_text_words.append(word)

# Собираем обратно в текст
result = " ".join(new_text_words)
print("Измененный текст:")
print(result)
