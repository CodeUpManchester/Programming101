import sys, os, random, time, msvcrt

ROW = 0
WALL_L = 1
WALL_R = 2

width = 30
height = 20
x = width / 2
y = height - 5
old_y = height - 5
gap_left = 0
gap_right = 0
ship = '**|**'
key = 255
play = True

def get_play_area(height):
    play_area = []
    for r in range(height):
        play_area.append(get_row(r, 0, 0))

    return play_area
        
def get_row(row_num, gap, shift):
    space = width - gap
    gap_left = shift if gap > 0 else 0
    row = (' ' * (gap + gap_left)) + '#' + (' ' * space) + '#'
    return row

# init
ship_size = len(ship)
if not ship_size % 2 == width % 2:
    width += 1
    x = width / 2

half_ship = ship_size / 2
if len(ship) % 2 == 1:
    half_ship += 1

x -= half_ship

play_area = get_play_area(height)

counter = 0
while play:
    counter += 1
    os.system('cls')

    play_area[old_y] = play_area[old_y].replace(ship, ' ' * len(ship))
    play_area = play_area[1:]
    play_area.append(get_row(height, counter / 20, random.randint(-1, 1)))
    play_area[y] = play_area[y][:x] + ship + play_area[y][x + len(ship):]

    if play_area[old_y].count('#') < 2:
        print 'GAME OVER'
        play = False
    
    for row in play_area:
        print row

    old_y = y

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

    if y < 0:
        y = 0
    if y >= height:
        y = height - 1

    time.sleep(0.02)
