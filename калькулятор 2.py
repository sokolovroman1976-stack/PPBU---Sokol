HISTORY_FILE = "calculations.txt"

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y

def log(result):
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(result + "\n")

def clear_history():
    with open(HISTORY_FILE, "w", encoding="utf-8"):
        pass
    print("История успешно стёрта.")

while True:
    print("\nВыберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Просмотр истории вычислений")

    choice = input("Введите номер операции (1/2/3/4/5): ")

    if choice == "5":



        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                print("\nИстория вычислений:")
                print(file.read(), end="")
        except FileNotFoundError:
            print("История пока пуста (файл не создан).")

        print()

            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))



    if choice == "1":
        result = add(num1, num2)
        operation = "+"
    elif choice == "2":
        result = subtract(num1, num2)
        operation = "-"
    elif choice == "3":
        result = multiply(num1, num2)
        operation = "*"
    elif choice == "4":
        result = divide(num1, num2)
        operation = "/"

    else:
        result = None
        print("Неверный ввод")



    if result is not None:
        message = f"Результат: {num1} {operation} {num2} = {result}"
        print(message)
        log(message)

    if input("Хотите посмотреть историю? (да/нет): ").strip().lower() == "да":
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                print("\nИстория вычислений:")
                print(file.read(), end="")
        except FileNotFoundError:
            print("История пока пуста (файл не создан).")

    if input("Хотите удалить историю? (да/нет): ").strip().lower() == "да":
        clear_history()

    if input("Хотите продолжить? (да/нет): ").strip().lower() != "да":
        print("Работа калькулятора завершена.")
        break