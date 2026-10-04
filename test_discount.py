"""test_discount.py - Тестирование алгоритма скидки."""
from datetime import datetime
from discount import calculate_price_with_discount


def run_tests():
    """Прогон тестов."""
    date = datetime(2026, 10, 15)  # предыдущий месяц = сентябрь 2026

    test_cases = [
        # (id, цена, ожидание, пояснение)
        (1, 80, 80, "Молоко — есть заказ 15.09 → без скидки"),
        (2, 500, 500, "Сыр — есть заказ 20.09 → без скидки"),
        (3, 40, 40, "Батон — есть заказ 25.09 → без скидки"),
        (4, 300, 225, "Куррица — нет заказов → 25% скидка"),
        (5, 50, 37.5, "Картофель — нет заказов → 25% скидка"),
        (6, 120, 90, "Яблоки — нет заказов → 25% скидка"),
        (7, 150, 112.5, "Сок — нет заказов → 25% скидка"),
    ]

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ")
    print("=" * 60)

    passed = 0
    for product_id, price, expected, comment in test_cases:
        result = calculate_price_with_discount(product_id, price, date)
        status = "✅" if result == expected else "❌"
        if result == expected:
            passed += 1
        print(f"{status} Товар {product_id}: {price} → {result} "
              f"(ожидалось {expected}) — {comment}")

    print("=" * 60)
    print(f"Пройдено: {passed} / {len(test_cases)}")


if __name__ == "__main__":
    run_tests()