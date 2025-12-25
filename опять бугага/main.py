print("1. РЕШЕТО ЭРАТОСФЕНА")

n = 30

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]]


print(f"Простые числа от 2 до {n}:")
primes = sieve(n)
print(primes)

print("\n2. ПЕРЕМЕШИВАНИЕ СЛОВ")

import random

text = input()


def shuffle_words(text):
    words = text.split()
    random.shuffle(words)
    return ' '.join(words)


print("Исходный текст:")
print(text)
print("\nПеремешанный текст:")
print(shuffle_words(text))

print("\n3. ОБНУЛЕНИЕ СТОЛБЦА МАТРИЦЫ")

matrix = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
]


def zero_column(matrix, col):
    for row in matrix:
        if col < len(row):
            row[col] = 0
    return matrix

print("Исходная матрица:")
for row in matrix:
    print(row)

col_index = 2
result_matrix = zero_column(matrix, col_index)

print(f"\nПосле обнуления столбца {col_index}:")
for row in result_matrix:
    print(row)