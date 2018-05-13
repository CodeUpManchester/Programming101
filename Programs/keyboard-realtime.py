import getch

while True:
    if getch.kbhit():
        key = ord(getch.getch())

        print (key)

        if key == 27:
            break
