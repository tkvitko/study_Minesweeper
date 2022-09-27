# Field structure
field_height = int(input("Playground height: "))
field_width = int(input("Playground width: "))
mines_count = int(input('Number of mines: '))

# Mine's coordinates
mines = []
for mine_number in range(mines_count):
    x_pos = int(input(f'X-coordinate of the mine {mine_number + 1}: '))
    y_pos = int(input(f'Y-coordinate of the mine {mine_number + 1}: '))
    mine = [x_pos, y_pos]
    mines.append(mine)

# Create blank playground
field = [[0 for i in range(field_width)] for j in range(field_height)]

# Set mines
for i in range(field_width):
    for j in range(field_height):
        for mine in mines:
            if mine[0] - 1 == i and mine[1] - 1 == j:
                field[i][j] = '*'

# Set numbers to the fields near mines
for i in range(field_height):
    for j in range(field_width):
        if field[i][j] != '*':  # only fields without mine
            count = 0  # mines around counter
            for x in [i - 1, i, i + 1]:  # X variations
                for y in [j - 1, j, j + 1]:  # Y variations
                    if field_height - 1 >= x >= 0 and field_width - 1 >= y >= 0:  # field boundaries
                        if field[x][y] == '*':  # if there is a mine
                            count += 1  # increment field counter

            field[i][j] = count

# Show playground
for line in field:
    print(line)
