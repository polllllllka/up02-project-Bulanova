
from db_products import get_all_products


def test_fields():
    
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


if __name__ == "__main__":
    test_fields()