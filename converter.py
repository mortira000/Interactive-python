# converter.py

# Константы для конвертации валют (относительно USD)
CURRENCY_RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "RUB": 92.5,
    "KZT": 480.0,
}

UNITS_BY_CATEGORY = {
    "Длина": ["Метры", "Километры", "Сантиметры", "Миллиметры", "Дюймы", "Мили"],
    "Масса": ["Килограммы", "Граммы", "Миллиграммы", "Тонны", "Фунты"],
    "Температура": ["Цельсий", "Фаренгейт", "Кельвин"],
    "Валюта": ["USD", "EUR", "RUB", "KZT"],
}


def convert_value(
    value: float, from_unit: str, to_unit: str, category: str
) -> float:
    if from_unit == to_unit:
        return value

    # 1. ДЛИНА (перевод через метры)
    if category == "Длина":
        to_meters = {
            "Метры": 1.0,
            "Километры": 1000.0,
            "Сантиметры": 0.01,
            "Миллиметры": 0.001,
            "Дюймы": 0.0254,
            "Мили": 1609.344,
        }
        meters = value * to_meters[from_unit]
        return meters / to_meters[to_unit]

    # 2. МАССА (перевод через килограммы)
    elif category == "Масса":
        to_kg = {
            "Килограммы": 1.0,
            "Граммы": 0.001,
            "Миллиграммы": 0.000001,
            "Тонны": 1000.0,
            "Фунты": 0.453592,
        }
        kg = value * to_kg[from_unit]
        return kg / to_kg[to_unit]

    # 3. ТЕМПЕРАТУРА
    elif category == "Температура":
        # Сначала переводим всё в Цельсий
        if from_unit == "Цельсий":
            celsius = value
        elif from_unit == "Фаренгейт":
            celsius = (value - 32) * 5 / 9
        elif from_unit == "Кельвин":
            celsius = value - 273.15

        # Переводим из Цельсия в целевую единицу
        if to_unit == "Цельсий":
            return celsius
        elif to_unit == "Фаренгейт":
            return (celsius * 9 / 5) + 32
        elif to_unit == "Кельвин":
            return celsius + 273.15

    # 4. ВАЛЮТА (перевод через USD)
    elif category == "Валюта":
        usd_value = value / CURRENCY_RATES[from_unit]
        return usd_value * CURRENCY_RATES[to_unit]

    raise ValueError("Неизвестная категория или единицы измерения")


if __name__ == "__main__":
    print("=== Тестирование модуля converter.py ===")
    print("10 дюймов в см:", convert_value(10, "Дюймы", "Сантиметры", "Длина"))
    print("100 кг в фунты:", convert_value(100, "Килограммы", "Фунты", "Масса"))
    print(
        "0 Цельсия в Фаренгейт:",
        convert_value(0, "Цельсий", "Фаренгейт", "Температура"),
    )
    print("100 USD в KZT:", convert_value(100, "USD", "KZT", "Валюта"))