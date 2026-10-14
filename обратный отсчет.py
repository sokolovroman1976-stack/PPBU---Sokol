# n = int(input())
# def safe_process_value(n):
#     if not (0 <= n <= 9999):
#         return "Ошибка: Некорректное значение n. Должно быть от 0 до 9999"
# s_n = str(n)
# a = s_n[0]
# b = s_n[1]
# c = s_n[2]
# d = s_n[3]
# print(a,\nb,\nc, \nd)
from string import digits

# n = int(input())
# def safe_process_value(n):
#     if not (0 <= n <= 9999):
#         return "Ошибка: Некорректное значение n. Должно быть от 0 до 9999"
#     digits = f"{n:04d}"
#     sum_digits = sum(int digits for digit in digits)
#     prod_digits = 1
#     for digit in digits:
#         prod_digits *= int(digit)
#
#
# return f"Тысячи:{digits[0]}\nСотни:{digits[1]}\nДесятки:{digits[2]}\nЕдиницы:{digits[3]}\nСумма цифр: {sum_digits}\nПроизведение цифр: {prod_digits}\nОбратный код:{digits[::-1]}"
#
# print(safe_process_value(n))


n = int(input())
def safe_process_value(n):
    if not (0 <= n <= 9999):
        return "Ошибка: Некорректное значение n. Должно быть от 0 до 9999"
    digits = f"{n:04d}"

    prod_digits = 1
    for digit in digits:
        prod_digits *= int(digit)

    return (
        f"Тысячи: {digits[0]}\n"
        f"Сотни: {digits[1]}\n"
        f"Десятки: {digits[2]}\n"
        f"Единицы: {digits[3]}\n"
        f"Сумма цифр: {(sum(int(digit) for digit in str(n)))}\n"
        f"Произведение цифр: {prod_digits}\n"
        f"Обратный код: {digits[::-1]}"
    )
print(safe_process_value(n))