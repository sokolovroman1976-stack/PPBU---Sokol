# def check_launch(fuel_available, fuel_required):
#     """
#     Проверяет, можно ли запускать аппарат.
#
#     Args:
#         fuel_available (float или int): фактический запас топлива.
#         fuel_required (float или int): минимально необходимый запас.
#
#     Returns:
#         str: 'Запуск разрешён', если топлива достаточно, иначе 'Запуск запрещён'.
#     """
#     if fuel_available >= fuel_required:
#         return 'Запуск разрешён'
#     else:
#         return 'Запуск запрещён'
#
#
# # Пример использования
# fuel_available = 500  # фактический запас
# fuel_required = 450  # минимально необходимый
#
# result = check_launch(fuel_available, fuel_required)
# print(result)  # Вывод: Запуск разрешён
#
# fuel_required = 600  # теперь запас меньше
# result = check_launch(fuel_available, fuel_required)
# print(result)  # Вывод: Запуск запрещён

num = 3
while num <= 43:
    print(num)
    num += 3

