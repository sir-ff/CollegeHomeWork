count = 0
for number in range(100, 10000):
    s_number = str(number)
    if len(s_number) == len(set(s_number)):
        count += 1
print(count)
