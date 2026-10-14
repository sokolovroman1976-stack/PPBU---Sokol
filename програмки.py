# num = 7564
# a = num % 10             # вычисляем последнюю цифру числа
# b = (num % 100) // 10    # вычисляем среднюю цифру числа
# c = ((num // 10 ** 2) % 10)
# d = num // 10 ** 3         # вычисляем первую цифру числа
#
# print(a)
# print(b)
# print(c)
# print(d)

# num = int(input())
# a = num % 10             # вычисляем последнюю цифру числа
# b = num // 10 % 10   # вычисляем среднюю цифру числа
# c = num // 100 % 10      # вычисляем первую цифру числа
#
#
# print (f'Сумма цифр = {a + b + c}')
# print(f'Произведение цифр =', a*b*c)

# a = input()
# b = ['тысяч', 'сотен', 'десятков', 'единиц']
# for i in range(4):
#     print('Цифра в позиции ' + b[i] + ' равна ' + a[i])








# a = int(input())
# b = int(input())
# n = (a + b)**2
# m = a**2 + b**2
#
# print(f'Квадрат суммы {a} и {b} равен {n}')

n = int(input())

nn = 10 * n + n
nnn = 100 * n + 10 * n + n

b = n + nn + nnn

print(b)
from itertools import permutations

# n = input('Введите число: ')
#
# unique_perms = set(permutations(n))
#
# for p in unique_perms:
#     num_str = ''.join(p)
#     # Преобразуем в int, чтобы убрать ведущие нули автоматически: '012' → 12
#     print(int(num_str))


num = int(input())
a = num % 10             # вычисляем последнюю цифру числа
b = num // 10 % 10   # вычисляем среднюю цифру числа
c = num // 100 % 10      # вычисляем первую цифру числа
print(c,b,a, sep="")
print(c,a,b, sep="")
print(b,c,a, sep="")
print(b,a,c, sep="")
print(a,c,b, sep="")
print(a,b,c, sep="")

# put your python code here
n = list(input())

for x in range( len(n)):
	for y in range( len(n)):
		for z in range( len(n)):
			if x != y and x != z and z != y:
				print(n[x] + n[y] + n[z])



