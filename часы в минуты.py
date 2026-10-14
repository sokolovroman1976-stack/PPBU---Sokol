n = int(input())
def safe_process_value(n):
    if not (0 <= n <= 1000000000):
        return "Ошибка: Некорректное значение n. Должно быть от 0 до 1439"
    d = n // 86400
    h = (n % 86400) // 3600
    m = (n % 3600) // 60
    s = n % 60
    return f"Дни: {d}\nЧасы: {h}\nМинуты: {m}\nСекунды: {s}"
print(safe_process_value(n))