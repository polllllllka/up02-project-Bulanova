
import tkinter as tk

from styles import (
    COLOR_MAIN_BG, COLOR_HIGHLIGHT,
    FONT_SIZE_NORMAL, FONT_SIZE_HEADER, font
)
from resources import get_product_image



def create_product_card(parent, product):
    
    qty = product.quantity
    bg_color = _get_card_color(qty)

    card = tk.Frame(parent, bg=bg_color, bd=1, relief="solid")
    card.pack(fill="x", padx=10, pady=5)

    _add_image(card, product, bg_color)
    _add_text_info(card, product, bg_color, qty)

    return card



def _get_card_color(qty):
    
    return COLOR_HIGHLIGHT if qty <= 3 else COLOR_MAIN_BG


def _indicator(qty):
    
    return "много" if qty > 5 else "мало"


def _add_image(card, product, bg_color):
    
    img_frame = tk.Frame(card, bg=bg_color)
    img_frame.pack(side="left", padx=10, pady=10)

   
    image_path = ""
    if product.image:
        image_path = f"resources/{product.image}"

    
    photo = get_product_image(image_path, size=(100, 100))
    if photo:
        img_label = tk.Label(img_frame, image=photo, bg=bg_color)
        img_label.image = photo   
        img_label.pack()
    else:
        tk.Label(img_frame, text="[НЕТ ФОТО]", bg=bg_color,
                 width=10, height=5).pack()


def _add_text_info(card, product, bg_color, qty):
   
    text_frame = tk.Frame(card, bg=bg_color)
    text_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)


    name = product.name if product.name else "[Без названия]"
    if len(name) > 100:
        name = name[:100] + "..."

    category = product.category if product.category else "[Без категории]"
    expiry = product.expiry_date if product.expiry_date else "[Не указан]"
    price = product.price if product.price is not None else 0

 
    price_str = f"{price:,.0f}".replace(",", " ")

   
    _add_label(text_frame, name,
               bg_color, bold=True, size=FONT_SIZE_HEADER)
    _add_label(text_frame, f"Категория: {category}", bg_color)
    _add_label(text_frame, f"Количество: {_indicator(qty)} ({qty} шт.)", bg_color)
    _add_label(text_frame, f"Срок годности: {expiry}", bg_color)
    _add_label(text_frame, f"{price_str} руб.",
               bg_color, bold=True, size=FONT_SIZE_HEADER, align="e")


def _add_label(parent, text, bg_color, bold=False,
               size=FONT_SIZE_NORMAL, align="w"):
    
    tk.Label(parent, text=text, font=font(size, bold=bold),
             bg=bg_color, anchor=align).pack(fill="x")