text = input("Введите текст: ")

count = 0
i = 0

while i < len(text):
    if text[i] in '.!?':
        count += 1
        while i < len(text) and text[i] in '.!?':
            i += 1
    else:
        i += 1

if len(text) > 0 and text[-1] not in '.!?':
    count += 1

print(f"В тексте найдено {count} предложений")