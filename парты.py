import math


def calculate_desks():
    try:
        # Ввод количества учеников для трёх классов
        class_1 = int(input())
        class_2 = int(input())
        class_3 = int(input())

        if class_1 < 0 or class_2 < 0 or class_3 < 0:
            print("Количество учеников не может быть отрицательным.")
            return

        # На одной парте сидят два ученика
        desks_1 = math.ceil(class_1 / 2)
        desks_2 = math.ceil(class_2 / 2)
        desks_3 = math.ceil(class_3 / 2)

        total_desks = desks_1 + desks_2 + desks_3

        print(f"Первый класс: {desks_1}")
        print(f"Второй класс: {desks_2}")
        print(f"Третий класс: {desks_3}")
        print(f"Всего парт: {total_desks}")

    except ValueError:
        print("Ошибка: пожалуйста, введите корректные целые числа.")


if __name__ == "__main__":
    calculate_desks()