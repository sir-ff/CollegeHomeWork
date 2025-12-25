def simple_counter(func):

    func.call_count = 0

    def wrapper(*args, **kwargs):
        func.call_count += 1

        print(f"\nФункция {func.__name__} вызвана {func.call_count} раз")
        print(f"Аргументы: {args}")

        result = func(*args, **kwargs)
        return result

    return wrapper

@simple_counter
def multiply(x, y):

    return x * y


@simple_counter
def greet(name, greeting="сушимонстерс"):
    return f"{greeting}, {name}!"

print("Умножение:")
print(f"Результат: {multiply(3, 4)}")
print(f"Результат: {multiply(5, 6)}")

print("\nПриветствие:")
print(f"Результат: {greet('АБАМА?')}")
print(f"Результат: {greet('U.S.AAAAAAAAAAAAAAAAA!', greeting='сушимонстерс)')}")