def f(name):
    # 1 
    name = name.replace('-', '_')
    return name
    # 2
    snake_case = []
    for char in name:
        if char.issuper():
            sneke_case.append('_' + char.lower())
        else:
            snake_case.append(char)
    name = ''.join(snake_case).strip('_')
    # 3
    name = name.replace(' ', '_')
    while '' in name:
        name = name.replace('', '_')
    name = name.strip('_')
    # 4
    if name and name[0].isdigit():
        name = name[1:]
    # 5
    chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_')
    if not all(char in chars for char in name):
        return "Введено некорректное имя переменной"
    return name

input_name = input("Введите имя переменной: ")

print(f(input_name))





