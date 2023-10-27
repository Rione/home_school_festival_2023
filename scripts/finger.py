#!/usr/bin/env python3
from hand_detect import finger_direction
# args : camera_id (default: 0)
# yield : direction ("R" | "L" | None)
# ESC to exit

n = -1
dir_list = ['0','0','0','0','0','0','0','0','0','0'] #からのリストを作った

for direction in finger_direction(): #連続してdirectionを出してる
  for val in (direction or []):
   pass

   while n<=8:
    n = n+1
    dir_list.insert(0+n,direction)
    rs = sum([s.endswith('R') for s in dir_list])
    ls = sum([s.endswith('L') for s in dir_list])
    print(dir_list)  
    if rs == 10:
      print('右')
      break
    elif ls == 10:
      print('左')
      break
    else:
       print('認識できませんでした')

  else:
   n = -1
   dir_list.clear()
   