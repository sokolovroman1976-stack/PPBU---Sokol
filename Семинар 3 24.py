# n = int(input())
# results = []
#
# for _ in range(n):
#     r, e = map(int, input().split())
#     score = 2 * r - e
#     results.append(score)
#
# # Выводим все вклады через пробел в исходном порядке
# print(*results)

# count = 0
#
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     count += 1
#
# print(count)

# b, p = list(map(int, input().split()))
#
# days = b // p      # количество оплаченных дней
# last = b % p       # остаток жетонов
#
# print(days, last)

# n = int(input())
#
# for i in range(n, 50, -2):
#     print(i)
#
# print("STOP")

# import re
# text = input()
# result = re.sub(r'\bCLUB\b', 'SECRET', text)
# print(result)


# import re
#
# text = input()
#
# # Заменяем только отдельное слово CLUB (точно такой регистр), не затрагивая club, CLUBHOUSE и т.п.
# # \b — граница слова, поэтому CLUB внутри CLUBHOUSE не заменяется
# result = re.sub(r'\bCLUB\b', 'SECRET', text)
#
# print(result)




# h, w = list(map(int, input().split()))
#
#
# # Выводим h строк, в каждой — w звёздочек
# for _ in range(h):
#     print('*' * w)

# h, w = list(map(int, input().split()))
#
# for i in range(h):
#     if i == 0 or i == h - 1:
#         # Верхняя и нижняя строки вся строка из звёздочек
#         print('*' * w)
#     else:
#         if w == 1:
#             # Если ширина 1, то этот пиксель и левый, и правый край, значит, '*'
#             print('*')
#         else:
#             # Боковые края *, внутри точки
#             print('*' + '.' * (w - 2) + '*')
# h, w = map(int, input().split())
#
# total = 0
#
# for _ in range(h):
#     row = list(map(int, input().split()))
#     total += sum(row)
#
# print(total)

h, w = map(int, input().split())

row_sums = []
for _ in range(h):
    row = list(map(int, input().split()))
    row_sums.append(sum(row))

print(*row_sums)


