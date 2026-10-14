# # n = int(input())
# # for i in range(1, n + 1):
# #     if i % 3 == 0 and i % 5 == 0:
# #         color = "BOTH"
# #     elif i % 3 == 0:
# #         color = "BLUE"
# #     elif i % 5 == 0:
# #         color = "RED"
# #     else:
# #         color = "WHITE"
# #
# #     print(f"{i} {color}")
#
# # Считываем n, l, r из первой строки
# # n = int(input())
# # l= int(input())
# # r = int(input())
# # count = 0 # количество принятых образцов
# # total_mass = 0 # суммарная масса принятых образцов
# #
# # # Обрабатываем каждую из n масс
# # for _ in range(n):
# #     mass = int(input())
# #     if l <= mass <= r:
# #         count = (count +1)
# #     total_mass += mass
# #
# # print(count, total_mass)
#
# # n = int(input())
# # l = int(input())
# # r = int(input())
# # count = 0
# # total_mass = 0
# # for _ in range(n):
# #     mass = int(input())
# #     if l <= mass <= r:
# #         count += count
# #         total_mass += mass
# #
# # print(count)
# # print(total_mass)
#
n = int(input())

# Считываем все уровни шума в список
noises = []
for _ in range(n):
    noises.append(int(input()))

# Находим минимальный уровень шума
min_noise = min(noises)

# Определяем номер первого появления (нумерация с 1)
first_index = noises.index(min_noise) + 1

# Считаем общее количество появлений минимума
count_min = noises.count(min_noise)

print(min_noise, first_index, count_min)
#
# # fio = input("Введите ФИО: ")
# #
# # f, i, o = fio.split()
# #
# # s = f"| {f} | {i} | {o} |"
# #
# # print(s)
#
# # b_1, q, n = int(input()), int(input()), int(input())
# # b_n = b_1 * (q ** (n-1))
# # print(f' {b_n}')
# #
# # s = int(input())
# # p = s//100
# # print(p)
#
#
# n = int(input())
#
# # Считываем все уровни шума в список
# noises = []
# for _ in range(n):
#  noises.Append(int(input()))
#
# # Находим минимальный уровень шума
# min_noise = min(noises)
#
# # Определяем номер первого появления (нумерация с 1)
# first_index = noises.Index(min_noise) + 1
#
# # Считаем общее количество появлений минимума
# count_min = noises.Count(min_noise)
#
# print(min_noise, first_index, count_min)
#
# a = int(input())
# if a % 2 == 0:
#     print(a // 2)
# else:
#     print(a // 2 + 1)
# 1minutes = int(input())
# print(f' {minutes} минут это - '{minutes//60})


minutes = int(input())
hours = minutes // 60
remaining_minutes = minutes % 60
print(
    f"{minutes} минут — это {hours} час и " f"{remaining_minutes} минут")