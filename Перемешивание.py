import random

n = int(input("Сколько значений будет участвовать? "))

values = []

for _ in range(n):
    values.append(input())

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

print("Исходный список:", values)
print("Перемешанный список:", shuffle_list(values))