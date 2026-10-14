# def celsius_to_fahrenheit(celsius):
#     return celsius * 9 / 5 + 32
#
#
# celsius = int(input())
# fahrenheit = celsius_to_fahrenheit(celsius)
#
# print(f"F = {fahrenheit}")

# n = int(input())
# m = int(input())
# p = int(input())
# if n < 0:
#     n = 0
# if m <0:
#     m = 0
# if p < 0:
#     p = 0
#
#
# print(n+m+p)

# v = int(input())
# print("детство" if v <= 13 else "молодость" if v <= 24 else "зрелость" if v <= 59 else "старость")

# age = int(input())
# if age>13:
#     if age>24:
#         if age>59:
#                 print('старость')
#         else:
#             print('зрелость')
#     else:
#         print('молодость')
# else:
#     print('детство')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if a > b:
#     a = b
# if c > d:
#     c = d
# if a > c:
#     a = c
#
# print(a)

a = int(input())

if a >= 2 and a <= 17:
    b = 3

else:
    b = 5

p = (a + b) * (a + b)
print(p)