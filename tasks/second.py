def print_table():
    print("| ID  | ProductName | Бренд        | Цена |")
    print("|-----|-------------|--------------|------|")
    for id, product in products.items():
        print(f"| {id} | {product['ProductName']:11} | {product['Бренд']:12} | {product['Цена']:3} |")

def read_id(product_id):
    if product_id in products:
        return products[product_id]["Цена"], products[product_id]["Бренд"]
    else:
        print("Товара с таким ID не существует")
        return None, None

def check_bill_validity(amount):
    valid_denominations = [10, 50, 100, 500]
    if amount in valid_denominations:
        return True
    else:
        print("Внесена фальшивая купюра")
        return False

def calculate_remaining(input_amount, amount_left):
    if input_amount >= amount_left:
        change = input_amount - amount_left
        print(f"Ваша сдача: {change} тугриков")
        return 0, change
    else:
        remaining = amount_left - input_amount
        print(f"Осталось внести {remaining} тугриков")
        return remaining, 0



# Примечание: выполнять данное задание с помощью функций выше необязательно, однако, возможно
# использование данных функций поможет вам на этапе размышлений о дизайне программы

# Your code here(づ ᴗ _ᴗ)づ♡

products = {
    "001": {"ProductName": "Батончик", "Бренд": "Snickers", "Цена": 70},
    "002": {"ProductName": "Вода", "Бренд": "Evian", "Цена": 45},
    "003": {"ProductName": "Газировка", "Бренд": "Coca-Cola", "Цена": 64},
    "004": {"ProductName": "Булочка", "Бренд": "Хлебзавод №1", "Цена": 33},
    "005": {"ProductName": "Чипсы", "Бренд": "Lays", "Цена": 55},
    "006": {"ProductName": "Шоколад", "Бренд": "Milka", "Цена": 80},
    "007": {"ProductName": "Сок", "Бренд": "J7", "Цена": 60},
    "008": {"ProductName": "Печенье", "Бренд": "Oreo", "Цена": 40},
    "009": {"ProductName": "Конфеты", "Бренд": "Alpen Gold", "Цена": 75},
    "010": {"ProductName": "Чай", "Бренд": "Lipton", "Цена": 30}
}

def vending_machine():
    print_table()

    product_id = input("Введите ID желаемого товара: ")
    if product_id == "ОТМЕНА":
        print("Программа завершена.")
        return

    try:
        product_id = int(product_id)
    except ValueError:
        print("Введено некорректное значение. Пожалуйста, введите число.")
        return

    product_price, product_brand = read_id(str(product_id).zfill(3))
    if product_price is None:
        return

    print(
        f"Вы выбрали {product_brand} {products[str(product_id).zfill(3)]['ProductName']}. Внесите {product_price} тугриков")

    total_inserted = 0
    amount_left = product_price

    while amount_left > 0:
        amount = input("Внесите купюру (или введите 'ОТМЕНА' для отмены): ")
        if amount == "ОТМЕНА":
            print("Программа завершена.")
            return

        try:
            amount = int(amount)
        except ValueError:
            print("Введено некорректное значение. Попробуйте снова.")
            continue

        if not check_bill_validity(amount):
            continue

        total_inserted += amount
        amount_left, change = calculate_remaining(amount, amount_left)

    print("Программа завершена.")


vending_machine()

