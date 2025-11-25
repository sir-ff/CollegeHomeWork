text = input("Введите текст: ")
words_input = input("Введите зарезервированные слова через пробел: ")

reserved_words = words_input.split()

text_words = text.split()

new_text_words = []

for word in text_words:
    word_clean = word
    if len(word) > 0:
        first_char = ''
        last_char = ''

        if word[0] in '.,!?;:':
            first_char = word[0]
            word_clean = word[1:]

        if word_clean and word_clean[-1] in '.,!?;:':
            last_char = word_clean[-1]
            word_clean = word_clean[:-1]

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

result = " ".join(new_text_words)
print("Измененный текст:")
print(result)
