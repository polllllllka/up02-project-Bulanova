"""test_discount.py - Расширенное тестирование алгоритма скидки.

Пара 6: тестирование, граничные случаи, отчёт.
"""
from datetime import datetime
from discount import calculate_price_with_discount


def print_test_report(passed, total):
    """ДЗ Задание 2: печатает отчёт о тестировании."""
    print("=" * 40)
    print("ОТЧЁТ О ТЕСТИРОВАНИИ")
    print(f"Пройдено: {passed} / {total}")
    if passed == total:
        print("Результат: ✅ УСПЕХ")
    else:
        print("Результат: ❌ ЕСТЬ ОШИБКИ")
    print("=" * 40)


def run_tests():
    """Прогон тестов."""
    test_cases = [
   
        (1, 80,  datetime(2026, 10, 15), 80,    "Молоко — заказ 15.09 → без скидки"),
        (2, 500, datetime(2026, 10, 15), 500,   "Сыр — заказ 20.09 → без скидки"),
        (3, 40,  datetime(2026, 10, 15), 40,    "Батон — заказ 25.09 → без скидки"),
        (4, 300, datetime(2026, 10, 15), 225,   "Куррица — нет заказов → 25% скидка"),
        (5, 50,  datetime(2026, 10, 15), 37.5,  "Картофель — нет заказов → скидка"),
        (6, 120, datetime(2026, 10, 15), 90,    "Яблоки — нет заказов → скидка"),
        (7, 150, datetime(2026, 10, 15), 112.5, "Сок — нет заказов → скидка"),

  
                
        (1, 80,  datetime(2026, 10, 1), 80,    "01.10 → сентябрь → заказ 15.09 → без скидки"),
        (2, 500, datetime(2026, 10, 1), 500,   "01.10 → сентябрь → заказ 20.09 → без скидки"),
        
        (4, 300, datetime(2026, 10, 1), 225,   "01.10 → сентябрь → заказов нет → скидка"),

       
        (1, 80,  datetime(2026, 10, 31), 80,    "31.10 → сентябрь → заказ есть"),
        (4, 300, datetime(2026, 10, 31), 225,   "31.10 → сентябрь → заказов нет → скидка"),

        
        (4, 0, datetime(2026, 10, 15), 0,      "Цена 0 → скидка 25% → всё равно 0"),

       
        (1, 80,  datetime(2026, 11, 15), 60,    "Ноябрь → октябрь без заказов → скидка"),
        (5, 50,  datetime(2026, 11, 15), 37.5,  "Ноябрь → октябрь без заказов → скидка"),
    ]

    print("=" * 70)
    print("РАСШИРЕННОЕ ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ")
    print("=" * 70)

    passed = 0
    for product_id, price, date, expected, comment in test_cases:
        result = calculate_price_with_discount(product_id, price, date)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        print(f"{status} Товар {product_id} на {date.date()}: "
              f"{price} → {result} (ожидалось {expected}) — {comment}")

    print()
    print_test_report(passed, len(test_cases))


if __name__ == "__main__":
    run_tests()