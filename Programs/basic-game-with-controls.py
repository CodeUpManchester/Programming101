import sys, os, time, msvcrt

play_area = []
width = 30
height = 20
x = width / 2
y = height - 5
gap_left = 0
gap_right = 0
ship = 'XX'
key = 255
play = True

for r in range(20):
    row_width = width
    if r == y:
        row_width -= len(ship)
    row = ''
    row += ' ' * gap_left
    row += '#'
    row += ' ' * (x - gap_left - 1)
    if r == y:
        row += ship
    else:
        row += ''
    row += ' ' * (row_width - x - gap_right - 1)
    row += '#'
    row += ' ' * gap_right
    play_area.append(row)

counter = 0
while play:
    counter += 1
    os.system('cls')

    for row in play_area:
        print row

    play_area[y] = play_area[y].replace(ship, ' ' * len(ship))

    if msvcrt.kbhit():        
        key = ord(msvcrt.getch())

        if key == 27: #Escape
            break
        if key == 224: #Arrow keys
            key = ord(msvcrt.getch())
            if key == 75: #Left
                x -= 1
            if key == 77: #Right
                x += 1
            elif key == 72: #Up
                y -= 1
            elif key == 80: #Down
                y += 1

    if x <= gap_left or x >= width - gap_right - len(ship):
        print 'GAME OVER'
        break
    if y < 0:
        y = 0
    if y >= height:
        y = height - 1

    if counter % 25 == 0:
        gap_left += 1
        gap_right += 1

    row = ''
    row += ' ' * gap_left
    row += '#'
    row += ' ' * (x - gap_left - 1)
    row += ' ' * (width - x - gap_right - 1)
    row += '#'
    row += ' ' * gap_right

    play_area = play_area[1:]
    play_area.append(row)

    for c in range(len(ship)):
        play_area[y] = play_area[y][:x] + ship + play_area[y][x+len(ship):]

    time.sleep(0.05)
