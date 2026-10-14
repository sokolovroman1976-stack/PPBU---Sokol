# def voice_price(words, rate=10):
#     return words * rate
# print(voice_price (4, 5))


# def has_pass(points, threshold=10):
#  return points >= threshold
# print(has_pass(points=4, threshold=7))
#

shift_point((2, 3), -1, 4)


# def shift_point(point, dx, dy):
#
#     x, y = point
#     return (x + dx, y + dy)
# # Пример использования:
# start_point = (3, 5)
# new_point = shift_point(start_point, -2, 10)
# print(new_point)  # Вывод: (1, 15)

# def best_score(scores):
#     if not scores:  # Проверяем, что список пуст
#         return None
#     return max(scores)  # Возвращаем наибольший элемент

# def add_vibe(values, bonus=1):
#     return [value + bonus for value in values]

def safe_values(values, limit):
 """
 Возвращает список только допустимых показаний датчика (от 0 до limit включительно).
 Порядок элементов и повторы сохраняются.

:param values: список чисел (показания датчика)
:param limit: верхняя граница допустимого диапазона (включительно)
:return: список допустимых значений
 """
 return [v for v in values if 0 <= v <= limit]

# Пример использования:
def safe_values(values, limit):
    result = safe_values(data, limit)
 print(result) # Вывод: [0, 5, 10, 7, 10]

def safe_values(values, limit):
    return [value for value in values if value <= limit]

def safe_values(values, limit):
    return [v for v in values if 0 <= v <= limit]

# Пример использования:
# if __name__ == "__main__":
#  data = [0, 5, 10, 15, 20, -3, 7, 10]
#  limit = 10
#  result = safe_values(data, limit)
#  print(result) # Вывод: [0, 5, 10, 7, 10]
#
#
# l = list(map(int, input(). split()))
# print(best_score(l)

# def learned_count(topics):
#  """
#  Возвращает количество разных названий тем.
#  Сравнение происходит точно, с учётом регистра.
#
# :param topics: список строк (названия тем)
# :return: целое число — количество уникальных тем
#  """
#  return len(set(topics))


