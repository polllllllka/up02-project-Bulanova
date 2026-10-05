"""catalog.py - Каталог товаров с карточками по макету."""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

from config import COLOR_HIGHLIGHT, FONT_FAMILY


def create_product_card(parent, product):
    
    
    qty = product.quantity
    bg_color = COLOR_HIGHLIGHT if qty <= 3 else "white"

    # Карточка 
    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)

    # Изображение 
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)

    # Имя картинки 
    image_name = product.image if product.image else "picture.png"
    image_path = os.path.join("resources", image_name)
    if not os.path.exists(image_path):
        image_path = os.path.join("resources", "picture.png")

    try:
        img = Image.open(image_path).resize((100, 100))
        photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(img_frame, image=photo, bg=bg_color)
        img_label.image = photo  
        img_label.pack()
    except Exception:
        tk.Label(img_frame, text="[ФОТО]", bg=bg_color,
                 width=10, height=5).pack()

    # Текстовая часть 
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    # Наименование 
    tk.Label(text_frame, text=product.name,
             font=(FONT_FAMILY, 14, "bold"),
             bg=bg_color, anchor="w").pack(fill="x")

    # Категория
    tk.Label(text_frame, text=f"Категория: {product.category}",
             font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")

    # Количество
    indicator = "много" if qty > 5 else "мало"
    tk.Label(text_frame, text=f"Количество: {indicator} ({qty} шт.)",
             font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")

    # Срок годности 
    tk.Label(text_frame, text=f"Срок годности: {product.expiry_date}",
             font=(FONT_FAMILY, 11), bg=bg_color, anchor="w").pack(fill="x")

    # Цена 
    tk.Label(text_frame, text=f"{product.price} руб.",
             font=(FONT_FAMILY, 14, "bold"),
             bg=bg_color, anchor="e").pack(fill="x")

    return card