grid = []

for x in range(10):
    grid.append([' ']*10)

old_x = 5
old_y = 5
x = 5
y = 5
grid[x][y] = '*'

for row in grid:
    print row

directions = ['LEFT', 'RIGHT', 'UP', 'DOWN']
diff_x = [-1, 1, 0, 0]
diff_y = [0, 0, -1, 1]

movement = ''
while (movement != 'exit'):
    movement = raw_input("Where now? ")

    old_x = x
    old_y = y

    for i in range(4):
        if movement == directions[i]:
            x += diff_x[i]
            y += diff_y[i]

    grid[old_y][old_x] = ' '
    grid[y][x] = '*'

    for row in grid:
        print row
