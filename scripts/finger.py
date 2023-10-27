#!/usr/bin/env python3
from hand_detect import finger_direction
# args : camera_id (default: 0)
# yield : direction ("R" | "L" | None)
# ESC to exit
import sys
from time import sleep

dir_list = [] #からのリストを作った

while True:
  for direction in finger_direction(): #連続してdirectionを出してる
    for val in (direction or []): #None 
      pass

      dir_list.append(direction)
      rs = sum([s.endswith('R') for s in dir_list])
      ls = sum([s.endswith('L') for s in dir_list])
      if len(dir_list)>29:
        dir_list.clear()

      if rs == 30 :
        print('右に向かいます')
        print('5秒後にカメラを閉じます')
        sleep(5)
        sys.exit()
      elif ls == 30:
        print('「  左に向かいます！  」')
        print('「  5秒後にカメラを閉じます...  」')
        sleep(5)
        sys.exit()
      else:
            print('...')