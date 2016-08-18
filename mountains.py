import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
hmax = 0
imax = 0

# game loop
while True:
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain, from 9 to 0.
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if mountain_h >= hmax:
        hmax = mountain_h
    # The number of the mountain to fire on.
    print(imax)
