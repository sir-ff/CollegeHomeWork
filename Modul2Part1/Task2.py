num1 = float(input())
num2 = float(input())
num3 = float(input())

choice = input()

if choice == 'максимум':
    maximum = max(num1, num2, num3)
    print(f": {maximum}")
elif choice == 'минимум':
    minimum = min(num1, num2, num3)
    print(f": {minimum}")
elif choice == 'арефмитическое':
    average = (num1 + num2 + num3) / 3
    print(f": {average}")
else:
    print()