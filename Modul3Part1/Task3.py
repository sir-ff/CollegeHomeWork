num1 = int(input("введите число: "))
num2 = int(input("введите число: "))

for num in range(num1,num2+1):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 != 0 and num % 5 != 0:
        print(num)