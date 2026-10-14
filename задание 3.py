car_info = input(
    "Введите данные об автомобиле "
    "(например: lada 2010г 205000км 450000руб.): ")

parts = car_info.split()

brand = parts[0]
year = parts[1]
mileage = parts[2]
price = parts[3]

print(f"Автомобиль: {brand}\n"f"Год выпуска: {year}\n"f"Пробег: {mileage}\n"f"Цена: {price}")