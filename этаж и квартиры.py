def find_floor_and_position(n, k):

    if n <= 0:
        return "Номер квартиры должен быть больше нуля.", None


    if k <= 0:
        return "Количество квартир на этаже должно быть больше нуля.", None



    floor = (n - 1) // k + 1
    position = (n - 1) % k + 1

    return floor, position


try:
    n = int(input())
    k = int(input())


    result_floor, result_position = find_floor_and_position(n, k)

    if isinstance(result_floor, int):
        print(f"Этаж: {result_floor}")
        print(f"Позиция на этаже: {result_position}")
    else:
        print(result_floor)

except ValueError:
    print("Ошибка: пожалуйста, вводите только целые числа.")