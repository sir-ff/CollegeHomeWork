class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self):
        print("Персонаж атакует!")

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Сила: {self.power})"


class Warrior(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp + 30, power + 5)  # увеличиваем здоровье и силу

    def attack(self):
        print("Воин наносит мощный удар мечом!")


class Mage(Character):
    def __init__(self, name, hp, power, mana):
        super().__init__(name, hp, power - 3)  # уменьшаем силу
        self.mana = mana  # добавляем ману

    def attack(self):
        print("Маг выпускает огненный шар!")

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, Сила: {self.power}, Мана: {self.mana})"


# Создаём список для хранения персонажей
characters = []

while True:
    print("\n=== Меню ===")
    print("1. Создать персонажа")
    print("2. Показать всех персонажей")
    print("3. Атака персонажа")
    print("4. Выход")

    choice = input(">>> ")

    if choice == "1":
        print("\nВыберите тип персонажа:")
        print("1. Воин")
        print("2. Маг")
        type_choice = input(">>> ")

        name = input("Введите имя персонажа: ")
        hp = int(input("Введите здоровье: "))
        power = int(input("Введите силу: "))

        if type_choice == "1":
            w = Warrior(name, hp, power)
            characters.append(w)
            print(f"Воин {name} создан!")
        elif type_choice == "2":
            mana = int(input("Введите ману: "))
            m = Mage(name, hp, power, mana)
            characters.append(m)
            print(f"Маг {name} создан!")
        else:
            print("Неправильный выбор!")

    elif choice == "2":
        if not characters:
            print("Персонажей пока нет.")
        else:
            print("\nСписок персонажей:")
            for i, char in enumerate(characters, 1):
                print(f"{i}. {char}")

    elif choice == "3":
        if not characters:
            print("Нет персонажей для атаки.")
        else:
            print("\nВыберите персонажа для атаки:")
            for i, char in enumerate(characters, 1):
                print(f"{i}. {char.name}")
            try:
                idx = int(input(">>> ")) - 1
                if 0 <= idx < len(characters):
                    characters[idx].attack()
                else:
                    print("Неправильный номер!")
            except ValueError:
                print("Введите число!")

    elif choice == "4":
        print("Выход из программы.")
        break

    else:
        print("Неправильный выбор, попробуйте снова.")