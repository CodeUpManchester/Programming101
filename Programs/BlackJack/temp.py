import time, msvcrt

raw_input("Press Enter key when ready")
start = time.clock()

while not msvcrt.getch():
    flag = False

finish = time.clock()

reaction = finish - start

output = "You took "
output += str(reaction)
output += " seconds"

print output
