import tkinter as tk
from tkinter import ttk
import requests
import json
import os

# Загружаем CURRENCIES из JSON
json_path = 'currencies.json'
if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        currencies = json.load(f)
else:
# Расширенный словарь: код → название валюты (запасной ариант)
    currencies = {
        'USD': 'Доллар США',
        'EUR': 'Евро',
        'GBP': 'Фунт стерлингов',
        'JPY': 'Японская йена',
        'CHF': 'Швейцарский франк',
        'CAD': 'Канадский доллар',
        'AUD': 'Австралийский доллар',
        'CNY': 'Китайский юань',
        'INR': 'Индийская рупия',
        'BRL': 'Бразильский реал',
        'ZAR': 'Южноафриканский рэнд',
        'KRW': 'Южнокорейская вона',
        'TRY': 'Турецкая лира',
        'SEK': 'Шведская крона',
        'NOK': 'Норвежская крона',
        'DKK': 'Датская крона',
        'PLN': 'Польский злотый',
        'CZK': 'Чешская крона',
        'HUF': 'Венгерский форинт',
        'RUB': 'Российский рубль',
        'KZT': 'Казахстанский тенге',
        'UZS': 'Узбекский сум',
        'UAH': 'Украинская гривна',
        'ILS': 'Израильский шекель',
        'SGD': 'Сингапурский доллар'
    }

def update_base_label(event):
    code = base_combobox.get()
    base_label.config(text=currencies.get(code, code))

def update_base2_label(event):
    code = base2_combobox.get()
    base2_label.config(text=currencies.get(code, code))

def update_wtarget_label(event):
    code = wtarget_combobox.get()
    wtarget_label.config(text=currencies.get(code, code))

def exchange():
    base_code = base_combobox.get().strip()
    base2_code = base2_combobox.get().strip()
    wtarget_code = wtarget_combobox.get().strip()

    # Проверка суммы
    amount_str = amount_entry.get().strip()
    try:
        amount = float(amount_str)
        if amount <= 0:
            result_label.config(text="Сумма должна быть больше нуля", fg="red")
            return
    except ValueError:
        result_label.config(text="Введите корректное число (например, 100 или 50.5)", fg="red")
        return

    if not base_code or not base2_code or not wtarget_code:
        result_label.config(text="Выберите все три валюты", fg="red")
        return

    try: # Запрос к API по базовой валюте
        response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}', timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get('result') != 'success':
            result_label.config(text="Ошибка API: неверный код валюты или сервис недоступен", fg="red")
            return

        rates = data.get('rates', {})

        if base2_code not in rates:
            result_label.config(text=f"Валюта {base2_code} не найдена в курсах", fg="red")
            return
        if wtarget_code not in rates:
            result_label.config(text=f"Валюта {wtarget_code} не найдена в курсах", fg="red")
            return

        rate_base2 = rates[base2_code]
        rate_target = rates[wtarget_code]

        base_name = currencies.get(base_code, base_code)
        base2_name = currencies.get(base2_code, base2_code)
        wtarget_name = currencies.get(wtarget_code, wtarget_code)

        rate_base1_to_target = rate_target
        rate_base2_to_target = rate_target / rate_base2
        converted_base1_to_target = amount * rate_base1_to_target
        converted_base2_to_target = amount * rate_base2_to_target

        msg = (
            f"{amount:,.2f} {base_name} ({base_code}) = "
            f"{converted_base1_to_target:,.2f} {wtarget_name} ({wtarget_code})\n\n"
            f"{amount:,.2f} {base2_name} ({base2_code}) = "
            f"{converted_base2_to_target:,.2f} {wtarget_name} ({wtarget_code})"
        )
        result_label.config(text=msg, fg="dark blue")

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
root.title('Курсы обмена валют с конвертацией (25 валют)')
root.geometry('420x540')

# Базовая валюта
tk.Label(root, text='Базовая валюта 1').pack(pady=(15, 0))
base_combobox = ttk.Combobox(root, values=list(currencies.keys()), state='readonly')
base_combobox.pack(pady=3)
base_combobox.set("USD")  # по умолчанию USD
base_combobox.bind('<<ComboboxSelected>>', update_base_label)

base_label = ttk.Label(root, font=('Arial', 9, 'bold'))
base_label.pack()
update_base_label(None)

# Базовая валюта 2
tk.Label(root, text='Базовая валюта 2').pack(pady=(15, 0))
base2_combobox = ttk.Combobox(root, values=list(currencies.keys()), state='readonly')
base2_combobox.pack(pady=3)
base2_combobox.set("EUR")  # по умолчанию EUR
base2_combobox.bind('<<ComboboxSelected>>', update_base2_label)

base2_label = ttk.Label(root, font=('Arial', 9, 'bold'))
base2_label.pack()
update_base2_label(None)

# Целевая валюта
tk.Label(root, text='В валюту').pack(pady=(15, 0))
wtarget_combobox = ttk.Combobox(root, values=list(currencies.keys()), state='readonly')
wtarget_combobox.pack(pady=3)
wtarget_combobox.set("RUB")  # по умолчанию RUB
wtarget_combobox.bind('<<ComboboxSelected>>', update_wtarget_label)

wtarget_label = ttk.Label(root, font=('Arial', 9, 'bold'))
wtarget_label.pack()
update_wtarget_label(None)

# Поле для суммы
ttk.Label(root, text="Сумма для обмена").pack(pady=(15, 0))
amount_entry = ttk.Entry(root)
amount_entry.pack(pady=5)
amount_entry.insert(0, "1")

# Кнопка
btn = tk.Button(root, text='Конвертировать', command=exchange)
btn.pack(pady=20)

# Результат в окне
result_label = tk.Label(
    root,
    text="Нажмите «Конвертировать», чтобы увидеть расчёт",
    font=('Arial', 10, 'bold'),
    justify='center',
    wraplength=600,
    height=3
)
result_label.pack(pady=10)

root.mainloop()
