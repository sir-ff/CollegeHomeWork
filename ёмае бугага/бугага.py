def load_notes():
    notes = []
    try:
        with open("notes.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and "|" in line:
                    parts = line.split("|", 1)
                    category = parts[0].strip()
                    text = parts[1].strip()
                    notes.append((category, text))
    except:
        pass
    return notes

def save_notes(notes):
    with open("notes.txt", "w", encoding="utf-8") as f:
        for category, text in notes:
            f.write(f"{category} | {text}\n")

def add_note():
    print("\n--- Добавление заметки ---")
    category = input("Категория: ")
    text = input("Текст заметки: ")

    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(f"{category} | {text}\n")
    print("Заметка добавлена!")

def show_all():
    notes = load_notes()
    print("\n--- Все заметки ---")
    if not notes:
        print("Заметок нет")
    else:
        for i, (category, text) in enumerate(notes, 1):
            print(f"{i}. [{category}] {text}")

def find_by_category():
    category = input("\nВведите категорию для поиска: ")
    notes = load_notes()
    found = []

    for cat, text in notes:
        if cat.lower() == category.lower():
            found.append((cat, text))

    print(f"\nНайдено в категории '{category}':")
    if found:
        for cat, text in found:
            print(f"- {text}")
    else:
        print("Ничего не найдено")

def search_by_word():
    word = input("\nВведите слово для поиска: ")
    notes = load_notes()
    found = []

    for category, text in notes:
        if word.lower() in text.lower():
            found.append((category, text))

    print(f"\nНайдено со словом '{word}':")
    if found:
        for cat, text in found:
            print(f"- [{cat}] {text}")
    else:
        print("Ничего не найдено")

def main():
    print("МЕНЕДЖЕР ЗАМЕТОК")

    while True:
        print("\n1. Добавить заметку")
        print("2. Показать все")
        print("3. Найти по категории")
        print("4. Найти по слову")
        print("5. Выход")

        choice = input("Выберите: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            show_all()
        elif choice == "3":
            find_by_category()
        elif choice == "4":
            search_by_word()
        elif choice == "5":
            print("Выход...")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()