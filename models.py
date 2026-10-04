"""Модели данных для проекта УП.02."""
from datetime import datetime
from discount import calculate_price_with_discount


class Product:
    """Класс Товар."""

    def __init__(self, product_id, category, name, expiry_date, price, quantity, image):
        self.id = product_id
        self.category = category
        self.name = name
        self.expiry_date = expiry_date
        self.price = price
        self.quantity = quantity
        self.image = image

    def total(self):
        """Общая стоимость партии."""
        return self.price * self.quantity

    def price_with_discount(self, discount_percent):
        """Цена со скидкой (вручную заданный процент)."""
        return self.price * (1 - discount_percent / 100)

    def price_with_discount_auto(self, date=None):
        """Цена со скидкой по алгоритму ДЭ (25%, если нет заказов)."""
        if date is None:
            date = datetime.now()
        return calculate_price_with_discount(self.id, self.price, date)
    


    def discounted_price(self):
        """Цена со скидкой 25% (упрощённо)."""
        return self.price * 0.75

    def indicator(self):
        """Индикатор много/мало."""
        return "много" if self.quantity > 5 else "мало"

    def is_available(self):
        """Есть ли товар в наличии."""
        return self.quantity > 0

    def info(self):
        """Строка с информацией."""
        availability = "✅ В наличии" if self.is_available() else "❌ Нет"
        return (
            f"{self.name} ({self.category}): {self.price} руб. | "
            f"Остаток: {self.quantity} шт. ({self.indicator()}) | "
            f"Срок: {self.expiry_date} | {availability}"
        )

