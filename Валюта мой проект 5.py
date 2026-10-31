from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests

# Словарь валют
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
    name = currencies[code]
    base_label.config(text=name)
    # base_label.config(text=currencies.get(code, code))
# Валюта Игорь
# def update_base_label(event):
#     code = base_combobox.get()
#     name = currencies[code]
#     base_label.config(text=name)

def update_base2_label(event):
    code = base2_combobox.get()
    base2_label.config(text=currencies.get(code, code))

def update_target_label(event):
    code = target_combobox.get()
    target_label.config(text=currencies.get(code, code))

def exchange():
    base_code = base_combobox.get().strip()
    base2_code = base2_combobox.get().strip()
    target_code = target_combobox.get().strip()

    # def exchange():
    #     target_code = target_combobox.get().strip()
    #     base_code = base_combobox.get().strip()
    #     # code = entry.get().upper().strip()
    #     # code = combobox.get()
    #     if target_code and base_code:
    #         try:
    if not base_code or not target_code:
        mb.showwarning('Внимание', 'Выберите базовые и целевую валюты')
        return

    try:
        response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}', timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get('result') != 'success':
            mb.showerror('Ошибка API', 'Неверный код валюты или сервис недоступен')
            return

        rates = data.get('rates', {})

        if target_code not in rates:
            mb.showerror('Ошибка', f'Валюта {target_code} не найдена в курсах')
            return

        rate_target = rates[target_code]
        base_name = currencies.get(base_code, base_code)
        target_name = currencies.get(target_code, target_code)

        # Курс для первой базовой валюты
        converted_base = 1 * rate_target
        msg = f"1 {base_name} = {converted_base:.2f} {target_name}\n"

        # Если выбрана вторая базовая валюта — добавляем сравнение
        if base2_code and base2_code != base_code:
            rate_base2 = rates[base2_code]
            base2_name = currencies.get(base2_code, base2_code)
            converted_base2 = rate_target / rate_base2
            msg += f"1 {base2_name} = {converted_base2:.2f} {target_name}"

        mb.showinfo('Курсы обмена', msg)

    except requests.exceptions.Timeout:
        mb.showerror('Ошибка', 'Превышено время ожидания ответа сервера')
    except requests.exceptions.ConnectionError:
        mb.showerror('Ошибка', 'Нет соединения с интернетом')
    except Exception as e:
        mb.showerror('Ошибка', str(e))

root = Tk()
root.title('Сравнение курсов (с messagebox)')
root.geometry('400x400')

# Базовая валюта 1
Label(root, text='Базовая валюта 1').pack(pady=(15, 0))
base_combobox = ttk.Combobox(root, values=list(currencies.keys()), state='readonly')
base_combobox.pack(pady=3, padx=10)
base_combobox.set("USD")
base_combobox.bind('<<ComboboxSelected>>', update_base_label)

base_label = ttk.Label(root, font=('Arial', 9, 'bold'))
base_label.pack()
update_base_label(None)

# Базовая валюта 2
Label(root, text='Базовая валюта 2').pack(pady=(15, 0))
base2_combobox = ttk.Combobox(root, values=list(currencies.keys()), state='readonly')
base2_combobox.pack(pady=3, padx=10)
base2_combobox.set("")
base2_combobox.bind('<<ComboboxSelected>>', update_base2_label)

base2_label = ttk.Label(root, font=('Arial', 9, 'bold'))
base2_label.pack()

# Целевая валюта
Label(root, text='Целевая валюта').pack(pady=(15, 0))
target_combobox = ttk.Combobox(root, values=list(currencies.keys()), state='readonly')
target_combobox.pack(pady=3, padx=10)
target_combobox.set("RUB")
target_combobox.bind('<<ComboboxSelected>>', update_target_label)

target_label = ttk.Label(root, font=('Arial', 9, 'bold'))
target_label.pack()
update_target_label(None)

btn = Button(root, text='Получить курсы', command=exchange)
btn.pack(pady=30)

root.mainloop()
