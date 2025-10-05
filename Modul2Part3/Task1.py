num = int(input('в ведите число от 1 до 100: '))

if num > 100:
    print('error')
elif num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
elif num % 3 != 0 and num % 5 != 0:
    print(num)