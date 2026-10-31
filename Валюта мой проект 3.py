import tkinter as tk
from tkinter import ttk
import requests

CURRENCIES = {
    'EUR': 'Евро',
    'USD': 'Доллар США',
    'JPY': 'Японская йена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'
}

def update_base_label(event):
    code = base_combobox.get()
    base_label.config(text=CURRENCIES.get(code, code))

def update_target_label(event):
    code = target_combobox.get()
    target_label.config(text=CURRENCIES.get(code, code))

def update_wtarget_label(event):
    code = wtarget_combobox.get()
    wtarget_label.config(text=CURRENCIES.get(code, code))

def exchange():
    base_code = base_combobox.get().strip()
    target_code = target_combobox.get().strip()
    wtarget_code = wtarget_combobox.get().strip()

    # Читаем и проверяем сумму
    amount_str = amount_entry.get().strip()
    try:
        amount = float(amount_str)
        if amount <= 0:
            result_label.config(text="Сумма должна быть больше нуля", fg="red")
            return
    except ValueError:
        result_label.config(text="Введите корректное число (например, 100 или 50.5)", fg="red")
        return

    # if not base_code or not target_code or not wtarget_code:
    #     result_label.config(text="Выберите все три валюты", fg="red")
    #     return

    try:
        response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}', timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get('result') != 'success':
            result_label.config(text="Ошибка API: неверный код валюты или сервис недоступен", fg="red")
            return

        rates = data.get('rates', {})

        if target_code not in rates:
            result_label.config(text=f"Валюта {target_code} не найдена в курсах", fg="red")
            return
        if wtarget_code not in rates:
            result_label.config(text=f"Валюта {wtarget_code} не найдена в курсах", fg="red")
            return

        rate1 = rates[target_code]
        rate2 = rates[wtarget_code]

        base_name = CURRENCIES.get(base_code, base_code)
        target_name = CURRENCIES.get(target_code, target_code)
        wtarget_name = CURRENCIES.get(wtarget_code, wtarget_code)

        converted1 = amount * rate1
        converted2 = amount * rate2

        # Формируем понятный вывод прямо в окне
        msg = (
            f"{amount:,.2f} {base_code} = {converted1:,.2f} {target_name}\n"
            f"{amount:,.2f} {base_code} = {converted2:,.2f} {wtarget_name}"
        )
        result_label.config(text=msg, fg="green")

    except requests.exceptions.Timeout:
        result_label.config(text="Ошибка: превышено время ожидания ответа сервера", fg="red")
    except requests.exceptions.ConnectionError:
        result_label.config(text="Ошибка: нет соединения с интернетом", fg="red")
    except requests.exceptions.HTTPError as e:
        result_label.config(text=f"Ошибка HTTP: {e}", fg="red")
    except Exception:
        result_label.config(text="Произошла непредвиденная ошибка", fg="red")

# Создаём окно
root = tk.Tk()
root.title('Сравнение трёх валют')
root.geometry('400x520')

# Базовая валюта
tk.Label(root, text='Из валюты (базовая)').pack(pady=(15, 0))
base_combobox = ttk.Combobox(root, values=list(CURRENCIES.keys()), state='readonly')
base_combobox.pack(pady=3)
base_combobox.current(1)  # USD
base_combobox.bind('<<ComboboxSelected>>', update_base_label)

base_label = ttk.Label(root, font=('Arial', 9, 'bold'))
base_label.pack()
update_base_label(None)

# Целевая валюта 1
tk.Label(root, text='В валюту 1').pack(pady=(15, 0))
target_combobox = ttk.Combobox(root, values=list(CURRENCIES.keys()), state='readonly')
target_combobox.pack(pady=3)
target_combobox.current(8)  # RUB
target_combobox.bind('<<ComboboxSelected>>', update_target_label)

target_label = ttk.Label(root, font=('Arial', 9, 'bold'))
target_label.pack()
update_target_label(None)

# Целевая валюта 2
tk.Label(root, text='В валюту 2').pack(pady=(15, 0))
wtarget_combobox = ttk.Combobox(root, values=list(CURRENCIES.keys()), state='readonly')
wtarget_combobox.pack(pady=3)
wtarget_combobox.current(0)  # EUR
wtarget_combobox.bind('<<ComboboxSelected>>', update_wtarget_label)

wtarget_label = ttk.Label(root, font=('Arial', 9, 'bold'))
wtarget_label.pack()
update_wtarget_label(None)

# Поле для суммы
ttk.Label(root, text="Сумма для обмена").pack(pady=(15, 0))
amount_entry = ttk.Entry(root)
amount_entry.pack(pady=5)
amount_entry.insert(0, "1")  # подсказка по умолчанию

# Кнопка
btn = tk.Button(root, text='Получить курсы', command=exchange)
btn.pack(pady=20)

# Результат прямо в окне (вместо messagebox)
result_label = tk.Label(
    root,
    text="Нажмите «Получить курсы», чтобы увидеть значения",
    font=('Arial', 10, 'bold'),
    justify='center',
    wraplength=360, height=3
)
result_label.pack(pady=10)


# ttk.Label(root, text="Сумма для обмена").pack(pady=(15, 0))
# amount_entry = ttk.Entry(root)
# amount_entry.pack(pady=5)

root.mainloop()
