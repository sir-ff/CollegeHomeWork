start = int(input("Введите начало диапозона: "))
end = int(input("Введите конец диапозона: "))
for i1 in range(start, end+1):
    for i2 in range(1, 10+1):
        result = i1 * i2
        print(f'{i1} х {i2} = {result}')
    print()