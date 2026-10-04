price = float(input("Введите цену: "))
percent = float(input("Введите скидку (%): "))
result = price * (1 - percent / 100)
print(f"Цена со скидкой: {result:.2f} руб.")
