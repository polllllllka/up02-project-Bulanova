"""test_catalog.py - Проверка вывода полей из БД."""
from db_products import get_all_products


def test_fields():
    """Проверяет, что все обязательные поля на месте."""
    products = get_all_products()
    print(f"Всего товаров: {len(products)}")

    errors = 0
    for p in products:
        if not p.name:
            print(f"❌ Товар id={p.id}: нет названия")
            errors += 1
        if p.price is None:
            print(f"❌ Товар id={p.id}: нет цены")
            errors += 1
        if p.quantity is None or p.quantity < 0:
            print(f"❌ Товар id={p.id}: некорректное количество")
            errors += 1

    if errors == 0:
        print("✅ Все товары содержат нужные поля")
    else:
        print(f"❌ Найдено ошибок: {errors}")


def test_prices():
    """У всех товаров есть цена (не None)."""
    products = get_all_products()
    for p in products:
        if p.price is None:
            print(f"❌ Товар id={p.id}: нет цены")
            return
    print("✅ У всех товаров есть цена")


def test_quantities():
    """У всех товаров количество ≥ 0."""
    products = get_all_products()
    for p in products:
        if p.quantity < 0:
            print(f"❌ Товар id={p.id}: отрицательное количество")
            return
    print("✅ У всех товаров количество ≥ 0")


def test_has_images():
    """Хотя бы у одного товара есть изображение."""
    products = get_all_products()
    with_image = [p for p in products if p.image]
    if with_image:
        print(f"✅ Товаров с изображением: {len(with_image)}")
    else:
        print("⚠️ Ни у одного товара нет изображения")


if __name__ == "__main__":
    test_fields()
    test_prices()
    test_quantities()
    test_has_images()