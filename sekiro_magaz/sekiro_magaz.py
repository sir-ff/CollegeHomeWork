products = {
    "Фрукты": [("Яблоки", 15, 60), ("Бананы", 10, 80), ("Апельсины", 5, 100)],
    "Овощи": [("Морковь", 20, 30), ("Картофель", 50, 25)],
    "Напитки": [("Вода", 100, 20), ("Сок", 30, 50)],
    "Молочные": [("Молоко", 40, 70)]
}

sekiro_items = {
    "Sekiro": [("1", 750), ("2_Stalin", 1250), ("3_LGBT die twice", 2750), ("предзаказ. 4",3250)]
}

print("ВСЕ ТОВАРЫ В МАГАЗИНЕ:")

for category, items in products.items():
    print(f"\n{category}:")
    for item in items:
        print(f"  {item[0]} --- {item[1]} шт., {item[2]} руб.")

print("ТОВАРЫ ИЗ SEKIRO:")

for category, items in sekiro_items.items():
    print(f"\n{category}:")
    for item in items:
        print(f"  {item[0]}, {item[1]} руб.")

print("АНАЛИЗ ОБЫЧНОГО МАГАЗИНА:")

most_expensive_item = None
most_expensive_price = 0

for category, items in products.items():
    for item in items:
        price = item[2]
        if price > most_expensive_price:
            most_expensive_price = price
            most_expensive_item = item
            most_expensive_category = category

print(f"Самый дорогой товар: {most_expensive_item[0]}")
print(f"Категория: {most_expensive_category}")
print(f"Цена: {most_expensive_item[2]} руб.")

print("\nАНАЛИЗ ТОВАРОВ SEKIRO:")

most_expensive_sekiro = None
most_expensive_sekiro_price = 0

for category, items in sekiro_items.items():
    for item in items:
        price = item[1]
        if price > most_expensive_sekiro_price:
            most_expensive_sekiro_price = price
            most_expensive_sekiro = item
            most_expensive_sekiro_category = category

print(f"Самый дорогой предмет Sekiro: {most_expensive_sekiro[0]}")
print(f"Категория: {most_expensive_sekiro_category}")
print(f"Цена: {most_expensive_sekiro[1]} руб.")

print("КАТЕГОРИИ С НАИБОЛЬШИМ КОЛИЧЕСТВОМ:")

max_quantity = 0
max_category = ""

for category, items in products.items():
    total_quantity = 0
    for item in items:
        total_quantity += item[1]

    print(f"Обычный магазин - '{category}': всего {total_quantity} шт.")

    if total_quantity > max_quantity:
        max_quantity = total_quantity
        max_category = category

print(f"\nВ обычном магазине больше всего товаров в категории: {max_category}")
print(f"Общее количество: {max_quantity} шт.")