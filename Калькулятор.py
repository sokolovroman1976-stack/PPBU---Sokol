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

# Файл для хранения истории
HISTORY_FILE = "calculations.txt"

def record_calculation(num1, num2, operation, result):
    """Записывает результат вычисления в файл истории."""
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{num1} {operation} {num2} = {result}\n")

# Пример базового калькулятора
def calculator():
    print("Выберите операцию: +, -, *, /")
    while True:
        operation = input("Операция: ").strip()
        if operation in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Первое число: "))
                num2 = float(input("Второе число: "))
            except ValueError:
                print("Ошибка: введите число.")
                continue

            # Выполняем вычисление
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)

            # Вывод результата
            print(f"Результат: {result}")

            # Запись в историю
            record_calculation(num1, num2, operation, result)
        else:
            print("Неизвестная операция")

        # Опция просмотра истории
        if input("Хотите посмотреть историю? (да/нет): ").strip().lower() == 'да':
            try:
                with open(HISTORY_FILE, 'r') as file:
                    print("\nИстория вычислений:")
                    for line in file:
                        print(line.strip())
            except FileNotFoundError:
                print("История пока пуста (файл не создан).")

# Запуск калькулятора
calculator()
