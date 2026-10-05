"""config.py - Константы проекта."""
import os

# Путь к БД
current_dir = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(current_dir, 'databases', 'db_variant_7.db')
if not os.path.exists(DB_PATH):
    DB_PATH = os.path.join(current_dir, 'db_variant_7.db')

# Константы для GUI
APP_TITLE = "Каталог товаров — УП.02"
FONT_FAMILY = "Calibri"
COLOR_HIGHLIGHT = "#ff8080"   # подсветка для товаров ≤3
COLOR_HEADER = "#D2F6E7"       # цвет шапки
