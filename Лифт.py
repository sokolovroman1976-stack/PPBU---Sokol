def solve_elevator():
    # Читаем первую строку: вместимость c, начальное число пассажиров s, число операций n
    c, s, n = map(int, input().split())

    current_passengers = s
    rejected_ops = 0

    # Обрабатываем n операций
    for _ in range(n):
        change = int(input())

        # Операция с нулём всегда допустима — ничего не меняем, но и не считаем отклонённой
        if change == 0:
            continue

        next_passengers = current_passengers + change

        # Проверяем, остаётся ли число пассажиров в допустимом диапазоне [0, c]
        if 0 <= next_passengers <= c:
            current_passengers += next_passengers
        else:
            # Операция отклоняется целиком
            rejected_ops += 1

    print(current_passengers, rejected_ops)



    solve_elevator()