valid_items = {"меч", "лук", "топор", "щит", "зелье"}

def input_items():
    while True:
        items = input("Введите предметы через пробел: ").strip().split()
        if all(item in valid_items for item in items):
            return items
        else:
            print("Неверный предмет, попробуйте снова")

adventurers_choices = []
for i in range(3):
    print(f"Авантюрист {i+1}:")
    choices = input_items()
    adventurers_choices.append(set(choices))

common_items = set.intersection(*adventurers_choices)

print(f"Количество предметов в общем наборе: {len(common_items)}")
