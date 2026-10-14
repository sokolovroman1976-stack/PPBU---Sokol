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
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Умножение")
    print("4 - Деление")
    print("5 - История")

    choice = input("Введите номер операции (1/2/3/4/5): ")

    if choice in ("1", "2", "3", "4"):
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == "1":
            operation = "+"
            result = add(num1, num2)
        elif choice == "2":
            operation = "-"
            result = subtract(num1, num2)
        elif choice == "3":
            operation = "*"
            result = multiply(num1, num2)
        else:
            operation = "/"
            result = divide(num1, num2)

        message = f"Результат: {num1} {operation} {num2} = {result:.2f}"
        print(message)
        log(message)

    elif choice == "5":
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as file:
                history = file.read()

            if history:
                print("\nИстория вычислений:")
                print("--------------------")
                print(history, end="")
                print("--------------------")
            else:
                print("История пока пуста.")
        except FileNotFoundError:
            print("История пока пуста (файл не создан).")

    else:
        print("Неверный ввод.")
        continue

    if input("Хотите продолжить? (да/нет): ").strip().lower() in ("да", "ls") :
        continue

    if input("Хотите удалить историю? (да/нет): ").strip().lower() in ("да", "ls"):
        clear_history()

    print("Работа калькулятора завершена.")
    break