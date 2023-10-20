#!/usr/bin/env python3
from hand_detect import finger_direction

# args : camera_id (default: 0)
# yield : direction ("R" | "L" | None)
# ESC to exit
counter_L = 0
counter_R = 0
limit = 10

for direction in finger_direction():
    if(direction == 'R'):
        counter_R += 1
    elif(direction == 'L'):
        counter_L += 1

    if(counter_R > limit or counter_L > limit):
        break
    

