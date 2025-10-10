while True:
    num = int(input("введите число: "))
    if num ==7:
        print("Good Bye")
        break
    elif num > 0:
        print("Number is positive")
    elif num < 0:
        print("Number is negative")
    else:
        print("Number is equal to zero")