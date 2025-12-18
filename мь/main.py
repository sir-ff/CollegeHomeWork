filename = input("Введите имя файла: ")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    total_words = 0
    total_chars = 0
    empty_lines = 0

    for line in lines:
        total_chars += len(line)

        if line.strip() == "":
            empty_lines += 1

        words = line.split()
        total_words += len(words)

    print(f"\nФайл: {filename}")
    print(f"Строк: {total_lines}")
    print(f"Слов: {total_words}")
    print(f"Символов: {total_chars}")
    print(f"Пустых строк: {empty_lines}")

except FileNotFoundError:
    print("Ошибка: файл не найден")