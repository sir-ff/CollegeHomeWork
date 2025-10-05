MILES = 0.000621371
INCHES = 39.3701
YARDS = 1.09361

meters = float(input())

while True:
    choice = input()
    if choice in ["мили", "дюймы", "ярды"]:
        break
    else:
        print("Error")

if choice == "мили":
    result = meters * MILES
    unit = "миль"
elif choice == "дюймы":
    result = meters * INCHES
    unit = "дюймов"
else:
    result = meters * YARDS
    unit = "ярдов"

print(f"{meters} {result:.2f} {unit}")