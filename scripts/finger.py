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
    
    if direction=="R": #Rのとき
        R=True
        L=False

    elif direction=="L": #Lのとき
        R=False
        L=True

    if direction=="R"and R==True:#Rが続いているとき
        i=i+1
        j=0
        print(i,j)#デバッグ

        if i>=10: #Rが１０回続いたとき
            print("右方向です")
            break
        
    elif direction=="L"and L==True:#Lが続いているとき
        j=j+1
        i=0
        print(i,j)#デバッグ
        if j>=10: #Rが１０回続いたとき
            print("左方向です")
            break   
        
    

        

