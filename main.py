import tkinter as tk
from tkinter import ttk


def convert():
    try:
        value = float(value_entry.get().replace(",", "."))
    except ValueError:
        result_label.config(text="Введите число, например 12.5")
        return

    conversion_name = conversion_box.get()

    if conversion_name == "Дюймы в сантиметры":
        converted = value * 2.54
    elif conversion_name == "Сантиметры в дюймы":
        converted = value / 2.54
    elif conversion_name == "Километры в мили":
        converted = value * 0.621371
    elif conversion_name == "Мили в километры":
        converted = value / 0.621371
    elif conversion_name == "Цельсий в Фаренгейт":
        converted = (value * 9 / 5) + 32
    elif conversion_name == "Фаренгейт в Цельсий":
        converted = (value - 32) * 5 / 9
    else:
        result_label.config(text="Выберите вариант из списка")
        return

    result_label.config(text=f"Результат: {converted:.2f}")


# Главное окно
root = tk.Tk()
root.title("Универсальный конвертер")
root.geometry("360x280")
root.resizable(False, False)

# Заголовок
title_label = ttk.Label(
    root, text="Конвертер величин", font=("Arial", 14, "bold")
)
title_label.pack(pady=10)

# Поле ввода значения
value_entry = ttk.Entry(root, font=("Arial", 11), justify="center")
value_entry.pack(pady=5)
value_entry.insert(0, "10")

# Выпадающий список
options = [
    "Дюймы в сантиметры",
    "Сантиметры в дюймы",
    "Километры в мили",
    "Мили в километры",
    "Цельсий в Фаренгейт",
    "Фаренгейт в Цельсий",
]

conversion_box = ttk.Combobox(
    root, values=options, state="readonly", font=("Arial", 10)
)
conversion_box.pack(pady=8)
conversion_box.current(0)

# Кнопка конвертации
convert_button = ttk.Button(root, text="Конвертировать", command=convert)
convert_button.pack(pady=8)

# Метка для вывода результата
result_label = ttk.Label(root, text="Результат: -", font=("Arial", 11, "bold"))
result_label.pack(pady=10)

root.mainloop()