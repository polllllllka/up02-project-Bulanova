
import tkinter as tk
from tkinter import ttk, messagebox

from styles import (
    COLOR_MAIN_BG, COLOR_SECONDARY_BG, COLOR_ACCENT,
    FONT_SIZE_NORMAL, FONT_SIZE_HEADER, FONT_SIZE_TITLE, font
)
from resources import get_product_image
from error_handler import validate_positive_int


class ViewForm:
  

    def __init__(self, parent, product, on_add_to_order=None):
       
        self.product = product
        self.on_add_to_order = on_add_to_order

        self.window = tk.Toplevel(parent)
        self.window.title(f"Просмотр — {product.name}")
        self.window.geometry("750x650")
        self.window.configure(bg=COLOR_MAIN_BG)

        self.build_ui()

    def build_ui(self):
        
        header = tk.Frame(self.window, bg=COLOR_SECONDARY_BG, height=60)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="КАРТОЧКА ТОВАРА",
                 font=font(FONT_SIZE_TITLE, bold=True),
                 bg=COLOR_SECONDARY_BG).pack(pady=15)

        
        main = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        main.pack(fill="both", expand=True, padx=20, pady=20)

        
        img_frame = tk.Frame(main, bg=COLOR_MAIN_BG)
        img_frame.pack(side="left", padx=10, anchor="n")

        image_path = ""
        if self.product.image:
            image_path = f"resources/{self.product.image}"

        photo = get_product_image(image_path, size=(200, 200))
        if photo:
            img_label = tk.Label(img_frame, image=photo, bg=COLOR_MAIN_BG)
            img_label.image = photo  
            img_label.pack()
        else:
            tk.Label(img_frame, text="[НЕТ ФОТО]", bg=COLOR_MAIN_BG,
                     width=15, height=10).pack()


        info_frame = tk.Frame(main, bg=COLOR_MAIN_BG)
        info_frame.pack(side="left", fill="both", expand=True, padx=20)

   
        name = self.product.name if self.product.name else "[Без названия]"
        category = self.product.category if self.product.category else "[Без категории]"
        expiry = self.product.expiry_date if self.product.expiry_date else "[Не указан]"
        price = self.product.price if self.product.price is not None else 0
        price_str = f"{price:,.0f}".replace(",", " ")
        qty = self.product.quantity
        status = "В наличии" if qty > 0 else "Нет в наличии"

        self._add_field(info_frame, "Наименование", name)
        self._add_field(info_frame, "Категория", category)
        self._add_field(info_frame, "Срок годности", expiry)
        self._add_field(info_frame, "Цена", f"{price_str} руб.")
        self._add_field(info_frame, "Количество", f"{qty} шт.")
        self._add_field(info_frame, "Статус", status)

    
        qty_input_frame = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        qty_input_frame.pack(fill="x", padx=20, pady=5)

        tk.Label(qty_input_frame, text="Количество для заказа:",
                 font=font(FONT_SIZE_NORMAL, bold=True),
                 bg=COLOR_MAIN_BG).pack(side="left")

        self.qty_entry = tk.Entry(qty_input_frame, width=10,
                                   font=font(FONT_SIZE_NORMAL))
        self.qty_entry.pack(side="left", padx=5)
        self.qty_entry.insert(0, "1")

   
        btn_frame = tk.Frame(self.window, bg=COLOR_MAIN_BG)
        btn_frame.pack(fill="x", pady=15)

        tk.Button(btn_frame, text="Добавить в заказ",
                  command=self.add_to_order,
                  bg=COLOR_ACCENT, fg="white",
                  font=font(FONT_SIZE_NORMAL),
                  padx=15, pady=5,
                  cursor="hand2").pack(side="left", padx=20)

        tk.Button(btn_frame, text="Назад",
                  command=self.window.destroy,
                  bg=COLOR_ACCENT, fg="white",
                  font=font(FONT_SIZE_NORMAL),
                  padx=15, pady=5,
                  cursor="hand2").pack(side="right", padx=20)

    def _add_field(self, parent, label, value):
        
        row = tk.Frame(parent, bg=COLOR_MAIN_BG)
        row.pack(fill="x", pady=3)

        tk.Label(row, text=f"{label}:",
                 font=font(FONT_SIZE_NORMAL, bold=True),
                 bg=COLOR_MAIN_BG, width=15, anchor="w").pack(side="left")
        tk.Label(row, text=str(value),
                 font=font(FONT_SIZE_NORMAL),
                 bg=COLOR_MAIN_BG, anchor="w").pack(side="left")

    def add_to_order(self):
        
        qty_str = self.qty_entry.get()
        ok, result = validate_positive_int(qty_str, "Количество")
        if not ok:
            messagebox.showwarning("Неверное значение", result)
            return

  
        if not self.on_add_to_order:
            messagebox.showinfo("Информация", "Функция в разработке")
            return

      
        if not self.product:
            messagebox.showerror("Ошибка", "Товар не выбран")
            return

      
        try:
            self.on_add_to_order(self.product)
            messagebox.showinfo("Успех",
                                f"Товар добавлен в заказ ({result} шт.)")
        except Exception as e:
            messagebox.showerror("Ошибка заказа",
                                 f"Не удалось добавить товар:\n{e}")