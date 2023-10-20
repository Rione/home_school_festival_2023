from hand_detect import finger_direction

# args : camera_id (default: 0)
# yield : direction ("R" | "L" | None)
# ESC to exit
for direction in finger_direction():
    print(direction)