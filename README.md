# Calculator Project

Простой калькулятор с функциями сложения и умножения.

## Функции
- **add(a, b)** - сложение двух чисел
- **multiply(a, b)** - умножение двух чисел

## Установка
```bash
git clone https://github.com/dglushchenko29/TRPOCP_2
cd TRPOCP_2
```

## Использование
```python
from calculator import add, multiply

# Примеры использования
result_add = add(2, 3)  # Вернет 5
result_multiply = multiply(2, 3)  # Вернет 6
```

## Запуск тестов
```bash
pytest test_calculator.py -v
```

## CI/CD Status
![Python CI](https://github.com/dglushchenko29/TRPOCP_2/actions/workflows/python-app.yml/badge.svg)

## Структура проекта
```
TRPOCP_2/
├── calculator.py      # Основной код калькулятора
├── test_calculator.py # Unit-тесты
├── README.md         # Документация
└── .github/workflows/
    └── python-app.yml # CI/CD конфигурация
```

## Версия
**Текущая версия:** 1.0.0

---

*Проект создан в рамках практической работы по CI/CD*
