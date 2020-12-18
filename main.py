# Ввод данных поля
field_height = int(input('Введите высоту поля: '))
field_width = int(input('Введите ширину поля: '))
mines_count = int(input('Введите количество мин: '))

# Ввод координат мин
mines = []
for mine_number in range(mines_count):
    x_pos = int(input(f'Введите x-координату мины {mine_number + 1}: '))
    y_pos = int(input(f'Введите y-координату мины {mine_number + 1}: '))
    mine = [x_pos, y_pos]
    mines.append(mine)

# Создание пустого поля
field = [[0 for i in range(field_width)] for j in range(field_height)]

# Расстановка мин
for i in range(field_width):
    for j in range(field_height):
        for mine in mines:
            if mine[0] - 1 == i and mine[1] - 1 == j:
                field[i][j] = '*'

# Расстановка чисел в клетках-соседях мин
for i in range(field_height):
    for j in range(field_width):
        if field[i][j] != '*':  # рассмотрим тлько клетки без мин
            count = 0  # счетчик мин вокруг
            for x in [i - 1, i, i + 1]:  # вариации изменения X
                for y in [j - 1, j, j + 1]:  # вариации изменения Y
                    if field_height - 1 >= x >= 0 and field_width - 1 >= y >= 0:    # не вылезаем за границы поля
                        if field[x][y] == '*':  # если вдруг там мина
                            count += 1  # растим счетчик

            field[i][j] = count

# Вывод поля
for line in field:
    print(line)
