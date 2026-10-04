"""db_products.py - Загрузка товаров из БД и работа с ними."""

import sqlite3
import os
from models import Product


current_dir = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(current_dir, 'databases', 'db_variant_7.db')
if not os.path.exists(DB_PATH):
    DB_PATH = os.path.join(current_dir, 'db_variant_7.db')
if not os.path.exists(DB_PATH):
    DB_PATH = os.path.join(os.path.dirname(current_dir), 'db_variant_7.db')


def get_connection():
    """Безопасная функция подключения к БД."""
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(
            f"База данных не найдена по пути: {DB_PATH}. "
            f"Проверьте, лежит ли файл db_variant_7.db в папке databases/ или проекта!"
        )
    return sqlite3.connect(DB_PATH)


def get_all_products():
    """Загружает все товары из БД в список объектов Product."""
    conn = get_connection()
    cur = conn.cursor()
    query = """
        SELECT id, категория, наименование, срок_годности, цена, количество, фото
        FROM Товар
        ORDER BY id
    """
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()

    products = []
    for row in rows:
        product = Product(
            product_id=row[0],
            category=row[1],
            name=row[2],
            expiry_date=row[3],
            price=row[4],
            quantity=row[5],
            image=row[6]
        )
        products.append(product)
    return products


def get_products_by_category(category_name):
    """Возвращает товары конкретной категории."""
    conn = get_connection()
    cur = conn.cursor()
    query = """
        SELECT id, категория, наименование, срок_годности, цена, количество, фото
        FROM Товар
        WHERE категория = ?
    """
    cur.execute(query, (category_name,))
    rows = cur.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append(Product(
            product_id=row[0],
            category=row[1],
            name=row[2],
            expiry_date=row[3],
            price=row[4],
            quantity=row[5],
            image=row[6]
        ))
    return products


def get_products_low_stock(threshold=3):
    """Возвращает товары с количеством ниже порога."""
    conn = get_connection()
    cur = conn.cursor()
    query = """
        SELECT id, категория, наименование, срок_годности, цена, количество, фото
        FROM Товар
        WHERE количество <= ?
    """
    cur.execute(query, (threshold,))
    rows = cur.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append(Product(
            product_id=row[0],
            category=row[1],
            name=row[2],
            expiry_date=row[3],
            price=row[4],
            quantity=row[5],
            image=row[6]
        ))
    return products


def print_products(products):
    """Выводит информацию о товарах."""
    print(f"\nВсего товаров: {len(products)}\n")
    for p in products:
        print(p.info())
        print("-" * 60)


def print_catalog_with_highlight(products):
    """Выводит каталог с подсветкой для товаров ≤3."""
    print(f"\n{'=' * 70}")
    print(f"КАТАЛОГ ({len(products)} товаров)")
    print("=" * 70)
    for p in products:
        highlight = "⚠️" if p.quantity <= 3 else "  "
        print(f"{highlight} {p.info()}")
    print("=" * 70)


if __name__ == "__main__":
    print("1. Все товары:")
    print_catalog_with_highlight(get_all_products())

    
    print("\n2. Товары категории «Молочное»:")
    print_catalog_with_highlight(get_products_by_category("Молочное"))

    
    print("\n3. Товары с низким остатком (≤20):")
    print_catalog_with_highlight(get_products_low_stock(20))