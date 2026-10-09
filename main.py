# main.py
import tkinter as tk
from tkinter import messagebox, ttk

from converter import UNITS_BY_CATEGORY, convert_value


class UnitConverterApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Универсальный Конвертер")
        self.root.geometry("450x520")
        self.root.resizable(False, False)

        self.history = []
        self.max_history_items = 5

        self.create_widgets()

    def create_widgets(self):
        # Выбор категории
        ttk.Label(
            self.root, text="Категория:", font=("Arial", 10, "bold")
        ).pack(anchor="w", padx=20, pady=(15, 2))
        self.category_box = ttk.Combobox(
            self.root,
            values=list(UNITS_BY_CATEGORY.keys()),
            state="readonly",
            font=("Arial", 10),
        )
        self.category_box.pack(fill="x", padx=20)
        self.category_box.current(0)
        self.category_box.bind("<<ComboboxSelected>>", self.on_category_change)

        # Поле ввода значения
        ttk.Label(self.root, text="Значение:", font=("Arial", 10, "bold")).pack(
            anchor="w", padx=20, pady=(10, 2)
        )
        self.value_entry = ttk.Entry(self.root, font=("Arial", 11))
        self.value_entry.pack(fill="x", padx=20)
        self.value_entry.insert(0, "1")

        # Выбор единиц "Из" и "В"
        units_frame = ttk.Frame(self.root)
        units_frame.pack(fill="x", padx=20, pady=10)

        left_frame = ttk.Frame(units_frame)
        left_frame.pack(side="left", expand=True, fill="x")

        ttk.Label(left_frame, text="Из:").pack(anchor="w")
        self.from_box = ttk.Combobox(
            left_frame, state="readonly", font=("Arial", 9)
        )
        self.from_box.pack(fill="x")

        # Кнопка быстрой смены единиц
        self.swap_btn = ttk.Button(
            units_frame, text="⇄", width=4, command=self.swap_units
        )
        self.swap_btn.pack(side="left", padx=8, pady=(15, 0))

        right_frame = ttk.Frame(units_frame)
        right_frame.pack(side="left", expand=True, fill="x")

        ttk.Label(right_frame, text="В:").pack(anchor="w")
        self.to_box = ttk.Combobox(
            right_frame, state="readonly", font=("Arial", 9)
        )
        self.to_box.pack(fill="x")

        # Обновляем списки единиц под начальную категорию
        self.update_unit_boxes()

        # Кнопка конвертации
        self.convert_btn = ttk.Button(
            self.root, text="Рассчитать", command=self.perform_conversion
        )
        self.convert_btn.pack(pady=10)

        # Вывод результата
        self.result_label = ttk.Label(
            self.root,
            text="Результат: -",
            font=("Arial", 12, "bold"),
            foreground="#1E88E5",
        )
        self.result_label.pack(pady=5)

        # История конвертаций
        ttk.Separator(self.root, orient="horizontal").pack(
            fill="x", padx=20, pady=10
        )
        ttk.Label(
            self.root,
            text=f"История (последние {self.max_history_items}):",
            font=("Arial", 10, "bold"),
        ).pack(anchor="w", padx=20)

        self.history_listbox = tk.Listbox(
            self.root, height=5, font=("Consolas", 9)
        )
        self.history_listbox.pack(fill="x", padx=20, pady=(5, 15))

    def update_unit_boxes(self):
        category = self.category_box.get()
        units = UNITS_BY_CATEGORY[category]

        self.from_box["values"] = units
        self.to_box["values"] = units

        self.from_box.current(0)
        self.to_box.current(1 if len(units) > 1 else 0)

    def on_category_change(self, event):
        self.update_unit_boxes()

    def swap_units(self):
        from_val = self.from_box.get()
        to_val = self.to_box.get()

        self.from_box.set(to_val)
        self.to_box.set(from_val)

    def perform_conversion(self):
        try:
            raw_value = self.value_entry.get().replace(",", ".")
            value = float(raw_value)
        except ValueError:
            messagebox.showerror(
                "Ошибка ввода", "Пожалуйста, введите корректное число!"
            )
            return

        category = self.category_box.get()
        from_unit = self.from_box.get()
        to_unit = self.to_box.get()

        try:
            result = convert_value(value, from_unit, to_unit, category)
            result_str = f"{value:g} {from_unit} = {result:.4g} {to_unit}"

            self.result_label.config(text=f"Результат: {result:.4g} {to_unit}")

            # Добавление в историю
            self.history.insert(0, result_str)
            if len(self.history) > self.max_history_items:
                self.history.pop()

            # Обновление Listbox
            self.history_listbox.delete(0, tk.END)
            for item in self.history:
                self.history_listbox.insert(tk.END, item)

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось выполнить конвертацию: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()