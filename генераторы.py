
# # Ввод мощностей трёх генераторов
# g1 = int(input())
# g2 = int(input())
# g3 = int(input())
#
# # Сначала найдём максимальную мощность через сравнения
# if g1 >= g2 and g1 >= g3:
#     max_power = g1
# elif g2 >= g1 and g2 >= g3:
#     max_power = g2
# else:
#     max_power = g3 # elif g3 >= g1 and g3 >= g2: max_power = g3
#
# # Теперь посчитаем, сколько генераторов имеют эту максимальную мощность
# leaders = 0
#
# if g1 == max_power:
#     leaders += 1
# if g2 == max_power:
#     leaders += 1
# if g3 == max_power:
#     leaders += 1
#
# print(f"Максимальная мощность: {max_power}")
# print(f"Количество лидеров: {leaders}")

temperatura = int(input())

if -100 <= temperatura <= 100:
    if temperatura < -20:
        print("Режим: ЭКСТРЕМАЛЬНЫЙ ХОЛОД")
    elif temperatura < 0:
        print("Режим: ХОЛОДНО")
    elif temperatura < 20:
        print("Режим: ПРОХЛАДНО")
    elif temperatura < 30:
        print("Режим: КОМФОРТНО")
    else:
        print("Режим: ЖАРКО")
else:
    print("Ошибка: температура должна быть в диапазоне от -100 до 100")