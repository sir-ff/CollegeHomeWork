start = int(input("Введите начало диапозона: "))
end = int(input("Введите конец диапазон: "))
for num in range(start,end):
        count = 0
        delitel = 2
        while delitel<num:
            if num%delitel == 0:
                count += 1
            delitel += 1
        if count == 0:
            print (f'{num} простое число')