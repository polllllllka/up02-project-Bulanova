
import sqlite3
from datetime import datetime
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(current_dir, "databases", "db_variant_7.db")
if not os.path.exists(DB_PATH):
    DB_PATH = os.path.join(current_dir, "db_variant_7.db")


def get_connection():
 
    return sqlite3.connect(DB_PATH)


def add_order_to_db(client, date=None):
   
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Заказ (дата, клиент) VALUES (?, ?)",
        (date, client)
    )
    conn.commit()
    order_id = cur.lastrowid
    conn.close()
    return order_id


def add_order_item(order_id, product_id, size, quantity, price):
  
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Состав_заказа "
        "(заказ_id, товар_id, размер, количество, цена) "
        "VALUES (?, ?, ?, ?, ?)",
        (order_id, product_id, size, quantity, price)
    )
    conn.commit()
    item_id = cur.lastrowid
    conn.close()
    return item_id


def create_order(client, items):
   
    conn = get_connection()
    cur = conn.cursor()
    try:
        date = datetime.now().strftime("%Y-%m-%d")
        cur.execute(
            "INSERT INTO Заказ (дата, клиент) VALUES (?, ?)",
            (date, client)
        )
        order_id = cur.lastrowid

        for product_id, size, quantity, price in items:
            cur.execute("SELECT количество FROM Товар WHERE id = ?", (product_id,))
            row = cur.fetchone()
            if not row or row[0] < quantity:
                raise ValueError(f"Недостаточно товара id={product_id}")

            cur.execute(
                "INSERT INTO Состав_заказа "
                "(заказ_id, товар_id, размер, количество, цена) "
                "VALUES (?, ?, ?, ?, ?)",
                (order_id, product_id, size, quantity, price)
            )

            cur.execute(
                "UPDATE Товар SET количество = количество - ? WHERE id = ?",
                (quantity, product_id)
            )

        conn.commit()
        return order_id
    except Exception as e:
        conn.rollback()
        print(f"Ошибка создания заказа: {e}")
        return None
    finally:
        conn.close()


def get_all_orders():
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, дата, клиент FROM Заказ ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_order_items(order_id):
   
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT
            Состав_заказа.id,
            Товар.наименование,
            Товар.категория,
            Состав_заказа.размер,
            Состав_заказа.количество,
            Состав_заказа.цена
        FROM Состав_заказа
        JOIN Товар ON Состав_заказа.товар_id = Товар.id
        WHERE Состав_заказа.заказ_id = ?
        ORDER BY Состав_заказа.id
    """, (order_id,))
    rows = cur.fetchall()
    conn.close()
    return rows


def get_order_total(order_id):
   
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT SUM(количество * цена)
        FROM Состав_заказа
        WHERE заказ_id = ?
    """, (order_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] or 0.0


def decrease_product_quantity(product_id, quantity):
    
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT количество FROM Товар WHERE id = ?", (product_id,))
        row = cur.fetchone()
        if not row or row[0] < quantity:
            return False
        cur.execute(
            "UPDATE Товар SET количество = количество - ? WHERE id = ?",
            (quantity, product_id)
        )
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Ошибка уменьшения: {e}")
        return False
    finally:
        conn.close()


def restore_product_quantity(product_id, quantity):
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE Товар SET количество = количество + ? WHERE id = ?",
        (quantity, product_id)
    )
    conn.commit()
    conn.close()


def update_product_quantity(product_id, new_quantity):
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE Товар SET количество = ? WHERE id = ?",
        (new_quantity, product_id)
    )
    conn.commit()
    conn.close()


def get_product_quantity(product_id):
  
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT количество FROM Товар WHERE id = ?", (product_id,))
    row = cur.fetchone()
    conn.close()
    return row[0] if row else 0


def get_last_order_id():
   
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT MAX(id) FROM Заказ")
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None