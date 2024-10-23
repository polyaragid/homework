import math

def f(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

N = int(input("Введите N: "))

x, y = 0, 0

for i in range(N):
    direction = input(f"Ход {i + 1}: ").strip().lower()
    steps = int(input(f"Количество шагов для хода {i + 1}: "))

    if direction == "вверх":
        y += steps
    elif direction == "вниз":
        y -= steps
    elif direction == "вправо":
        x += steps
    elif direction == "влево":
        x -= steps
    else:
        print("Неверное направление. Используйте 'вверх', 'вниз', 'вправо' или 'влево'.")
        break

print(f(0, 0, x, y))
