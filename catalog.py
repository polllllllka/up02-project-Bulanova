"""catalog.py - Каталог товаров с карточками по макету."""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from resources import get_product_image

from styles import (
    COLOR_MAIN_BG, COLOR_HIGHLIGHT,
    FONT_FAMILY, FONT_SIZE_NORMAL, FONT_SIZE_HEADER,
    font
)


def create_product_card(parent, product):
    
    
    qty = product.quantity
    bg_color = COLOR_HIGHLIGHT if qty <= 3 else "white"

    # Карточка 
    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)

    # Изображение 
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)

    
    # Картинка товара или заглушка
    image_path = ""
    if product.image:
        image_path = os.path.join("resources", product.image)

    photo = get_product_image(image_path, size=(100, 100))
    if photo:
        img_label = tk.Label(img_frame, image=photo, bg=bg_color)
        img_label.image = photo
        img_label.pack()
    else:
        tk.Label(img_frame, text="[НЕТ ФОТО]", bg=bg_color,
                 width=10, height=5).pack()
    # Текстовая часть 
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    # Наименование 
    tk.Label(text_frame, text=product.name,
             font=font(FONT_SIZE_HEADER, bold=True),
             bg=bg_color, anchor="w").pack(fill="x")

    # Категория
    tk.Label(text_frame, text=f"Категория: {product.category}",
             font=font(FONT_SIZE_NORMAL), bg=bg_color, anchor="w").pack(fill="x")

    # Количество
    indicator = "много" if qty > 5 else "мало"
    tk.Label(text_frame, text=f"Количество: {indicator} ({qty} шт.)",
             font=font(FONT_SIZE_NORMAL), bg=bg_color, anchor="w").pack(fill="x")

    # Срок годности 
    tk.Label(text_frame, text=f"Срок годности: {product.expiry_date}",
             font=font(FONT_SIZE_NORMAL), bg=bg_color, anchor="w").pack(fill="x")

    # Цена 
    tk.Label(text_frame, text=f"{product.price} руб.",
             font=font(FONT_SIZE_HEADER, bold=True),
             bg=bg_color, anchor="e").pack(fill="x")
    
    # Разделитель снизу
    sep = tk.Frame(parent, height=1, bg="#cccccc")
    sep.pack(fill="x", padx=20, pady=2)

    return card