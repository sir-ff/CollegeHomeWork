products = {
    "Фрукты": [("Яблоки", 15, 60), ("Бананы", 10, 80), ("Апельсины", 20, 70)],
    "Овощи": [("Морковь", 20, 30), ("Помидоры", 15, 100)],
    "Напитки": [("Сок", 30, 120), ("Вода", 50, 40)],
    "Молочные": [("Молоко", 25, 80), ("Сыр", 10, 300)]
}

print("ВСЕ ТОВАРЫ В МАГАЗИНЕ")
print()

for category, items in products.items():
    print(f"{category}:")
    for item in items:
        name = item[0]
        count = item[1]
        price = item[2]
        print(f"  {name},{count} шт., {price} руб.")
    print()

print("ПОИСК САМОГО ДОРОГОГО ТОВАРА")
most_expensive_name = ""
most_expensive_price = 0
most_expensive_category = ""

for category, items in products.items():
    for item in items:
        name = item[0]
        price = item[2]

        if price > most_expensive_price:
            most_expensive_price = price
            most_expensive_name = name
            most_expensive_category = category

print(f"Самый дорогой товар: {most_expensive_name}")
print(f"Цена: {most_expensive_price} руб.")
print(f"Категория: {most_expensive_category}")
print()

print("КАТЕГОРИЯ С БОЛЬШИМ КОЛИЧЕСТВОМ ТОВАРОВ")

max_count = 0
max_category = ""

for category, items in products.items():
    total_in_category = 0

    for item in items:
        count = item[1]
        total_in_category += count

    print(f"{category}: всего {total_in_category} шт.")

    if total_in_category > max_count:
        max_count = total_in_category
        max_category = category

print(f"Больше всего товаров в категории: {max_category}")
print(f"Общее количество: {max_count} шт.")
print()

print("ОБЩАЯ СТОИМОСТЬ ВСЕХ ТОВАРОВ")

total_cost = 0

for category, items in products.items():
    for item in items:
        name = item[0]
        count = item[1]
        price = item[2]

        item_cost = count * price
        total_cost += item_cost

print(f"Общая стоимость всех товаров: {total_cost} руб.")
print("jotaro ты любишь кабочки?")
print("Dio запони раз и навсега и их блин ненавижу!!!!!")