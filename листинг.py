#
# # i = 100
# #
# # while i >= 1:
# #
# #     print(i)
# #
# #     i -=10
#
# def generate_pythagorean_triples(N):
#     """Генерирует все пифагоровы тройки, где c <= N."""
#     triples = []
#     for c in range(1, N + 1):
#         for a in range(1, c):
#             for b in range(a, c):
#                 if a**2 + b**2 == c**2:
#                     triples.append((a, b, c))
#     return triples
#
# # Пример
# N = int(input("Введите N: "))
# triples = generate_pythagorean_triples(N)
# for triple in triples:
#     print(*triple)

a = 8
b = a+1
c = a+2
print(a, b, c, sep='\n')
