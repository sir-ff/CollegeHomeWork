karamba = input("выбирете значение(+,-,*,/): ")

if "+" in karamba:
    a,b = karamba.split("+")
    print(float(a) + float(b))
elif "-" in karamba:
    a,b = karamba.split("-")
    print(float(a) - float(b))
elif "*" in karamba:
    a,b = karamba.split("*")
    print(float(a) * float(b))
elif "/" in karamba:
    a,b = karamba.split("/")
    print(float(a) / float(b))
else:
    print("ну как бы нет, понял? :)")
