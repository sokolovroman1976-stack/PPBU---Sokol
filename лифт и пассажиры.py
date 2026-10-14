def solve_elevator(c, s, operations):
    """
    c — вместимость лифта (макс. число пассажиров)
    s — начальное число пассажиров
    operations — список операций (положительные: вход, отрицательные: выход, 0: без изменений)

    Возвращает: (итоговое число пассажиров, количество отклонённых операций)
    """
    current_passengers = s
    rejected_count = 0

    for op in operations:
        next_passengers = current_passengers + op

        # Проверяем, остаётся ли число пассажиров в допустимом диапазоне [0, c]
        if 0 <= next_passengers <= c:
            current_passengers = next_passengers
        else:
            rejected_count += 1
            # При отклонении операция не применяется, current_passengers не меняется

    return current_passengers, rejected_count


# Пример использования:
if __name__ == "__main__":
    c = 10  # вместимость
    s = 3  # начальное количество пассажиров
    ops = [5, -2, 8, -15, 0, 4, -3]  # операции

    result_passengers, result_rejected = solve_elevator(c, s, ops)
    print(f"Итоговое число пассажиров: {result_passengers}")
    print(f"Количество отклонённых операций: {result_rejected}")
