# s1 = int(input())
# i = color("red")
# for i in range(1, s1+1):
#      for j in range(i, i*s1+1, i):
#          print(j, end='\t')
#      print()

def print_pythagorean_table():
    n = 10
    RED = "\033[1;31m"
    RESET = "\033[0m"
    # Верхняя строка с заголовками столбцов
    print(f"{RED}{' ':>3}{RESET}", end=" ")
    for j in range(1, n + 1):
        print(f"{RED}{j:3}{RESET}", end=" ")
    print()
    # Строки таблицы
    for i in range(1, n + 1):
        # Заголовок строки
        print(f"{RED}{i:3}{RESET}", end=" ")
        # Значения произведений
        for j in range(1, n + 1):
            print(f"{i * j:3}", end=" ")
        print()
print_pythagorean_table()

print()
print()
for i in range(1, 10):
   for j in range(1, 10):
       print(i, '*', j, '=', i * j, end='\t\t')
   print()