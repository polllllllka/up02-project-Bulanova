"""discount.py - Алгоритм расчёта скидки 25%.

Скидка применяется к товарам, по которым НЕ было заказов
в предыдущем календарном месяце относительно даты расчёта.
"""
import os
import sqlite3
from datetime import datetime, timedelta


current_dir = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(current_dir, 'databases', 'db_variant_7.db')


if not os.path.exists(DB_PATH):
    raise FileNotFoundError(f"БД не найдена: {DB_PATH}")


def get_previous_month_range(date):
    """Возвращает (начало, конец) предыдущего месяца."""
    first_day = date.replace(day=1)
    last_day_prev = first_day - timedelta(days=1)
    first_day_prev = last_day_prev.replace(day=1)
    return (
        first_day_prev.strftime("%Y-%m-%d"),
        last_day_prev.strftime("%Y-%m-%d")
    )


def has_orders_in_previous_month(product_id, date):
    """Есть ли заказы товара в предыдущем месяце?"""
    start, end = get_previous_month_range(date)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    cur.execute(
        "SELECT COUNT(*) FROM Заказ "
        "WHERE товар_id = ? AND дата BETWEEN ? AND ?",
        (product_id, start, end)
    )
    count = cur.fetchone()[0]
    conn.close()
    return count > 0


def calculate_price_with_discount(product_id, price, date):
    """Рассчитывает цену со скидкой 25% для товаров без заказов в прошлом месяце."""
    if has_orders_in_previous_month(product_id, date):
        return price
    return price * 0.75