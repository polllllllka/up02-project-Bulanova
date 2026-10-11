
from db_products import get_all_products


def test_db_available():
    try:
        products = get_all_products()
        return isinstance(products, list)
    except Exception as e:
        print(f"❌ БД недоступна: {e}")
        return False


def test_products_count():
    products = get_all_products()
    return len(products) > 0


def test_product_fields():
    products = get_all_products()
    for p in products:
        required = ["id", "name", "category", "expiry_date",
                    "price", "quantity", "image"]
        for field in required:
            if not hasattr(p, field):
                print(f"❌ Товар id={p.id}: нет поля {field}")
                return False
    return True


def test_prices_are_numbers():
    products = get_all_products()
    for p in products:
        if not isinstance(p.price, (int, float)):
            print(f"❌ Товар id={p.id}: цена не число ({type(p.price)})")
            return False
    return True


def test_quantity_not_negative():
    products = get_all_products()
    for p in products:
        if p.quantity < 0:
            print(f"❌ Товар id={p.id}: отрицательное количество")
            return False
    return True


def test_names_not_empty():
    products = get_all_products()
    for p in products:
        if not p.name:
            print(f"❌ Товар id={p.id}: пустое название")
            return False
    return True


def test_has_images():
    products = get_all_products()
    with_image = [p for p in products if p.image]
    return len(with_image) > 0


def run_all_tests():
    tests = [
        ("БД доступна", test_db_available),
        ("Товары загружены", test_products_count),
        ("У всех товаров нужные поля", test_product_fields),
        ("Все цены — числа", test_prices_are_numbers),
        ("Количество не отрицательное", test_quantity_not_negative),
        ("Названия не пустые", test_names_not_empty),
        ("Хотя бы одно фото есть", test_has_images),
    ]

    print("=" * 60)
    print("ТЕСТИРОВАНИЕ КАТАЛОГА")
    print("=" * 60)

    passed = 0
    for name, func in tests:
        result = func()
        status = "✅" if result else "❌"
        if result:
            passed += 1
        print(f"{status} {name}")

    print("=" * 60)
    print(f"Пройдено: {passed} / {len(tests)}")


if __name__ == "__main__":
    run_all_tests()