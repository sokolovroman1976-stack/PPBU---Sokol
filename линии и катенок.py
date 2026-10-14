# # Вводим фактический запас топлива
# actual_fuel = int(input())
#
# # Вводим минимальный необходимый запас топлива
# minimum_fuel = int(input())
#
# # Проверяем условие запуска
# if actual_fuel > minimum_fuel:
#     print("Статус: ЗАПУСК РАЗРЕШЁН")
# elif actual_fuel < minimum_fuel:
#     print("Статус: ЗАПУСК ЗАПРЕЩЁН")
# elif actual_fuel == minimum_fuel:
#     print("Статус: ЗАПУСК РАЗРЕШЁН")

number = int(input())
if number < 0:
    print("Положение: СЛЕВА")
elif number > 0:
    print("Положение: СПРАВА")
elif number == 0:
    print("Положение: В БАЗЕ")
