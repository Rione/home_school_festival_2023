from hand_detect import finger_direction

# args : camera_id (default: 0)
# yield : direction ("R" | "L" | None)
# ESC to exit

r = 0
l = 0

for direction in finger_direction():
    print(direction)

    if direction  == "R":
        r += 1
        
    if r > 10:
            print("right")
            break
        
    elif direction  == "L":
        l += 1
    if l > 10:
            print("left")
            break