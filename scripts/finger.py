from hand_detect import finger_direction

# args : camera_id (default: 0)
# yield : direction ("R" | "L" | None)
# ESC to exit
i=0
j=0
R=True #一つ前がRだったか
L=True #一つ前がLだったか
for direction in finger_direction():
    print(direction)
    
    if direction=="R"and R==True: #Rが続いているとき
        R=True
        L=False
        i=i+1
        j=0
        if i>=10: #Rが１０回続いたとき
            print("右方向です")
            break
            
            
    elif direction=="L"and L==True: #Lが続いているとき
        R=False
        L=True
        i=0
        j=j+1
        if j>=10: #Lが１０回続いたとき
            print("左方向です")
            break

        

