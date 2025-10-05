tariffs = {
    "билайн": {
        "между собой": 1,
        "между другими": 3
    },
    "мтс": {
        "между собой": 0,
        "между другими": 7
    },
    "мегафон": {
        "между собой": 2,
        "между другими": 5
    }
}
minutes = int(input("в ведите число (в минутах): "))
from_operator = input("выберете оператора с которого звоните(мтс,билайн,мегафон): ").lower()
to_operator = input("выберете оператора которому звоните(мтс,билайн,мегафон): ").lower()
price = 0
if from_operator == to_operator:
    rate = tariffs[from_operator] ["между собой"]
    price = minutes * rate
else:
    rate = tariffs[from_operator] ["между другими"]
    price = minutes * rate
print(f"стоимость разговора составит: {price}")