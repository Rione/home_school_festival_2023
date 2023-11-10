#!/usr/bin/env python3
from hand_detect import finger_direction
# args : camera_id (default: 0)
# yield : direction ("R" | "L" | None)
# ESC to exit
import sys
from time import sleep
import rospy
from std_msgs.msg import String

def l_or_r():
    rospy.Publisher('topic_direction', String, queue_size=10) #topicは情報の名前 pub=(topic)=>lis
    rospy.init_node('finger_node', anonymous=True) #finger_nodeはpublisherのノード　pub=>lis
    r = rospy.Rate(10) # 10hz

    dir_list = [] #からのリストを作った

    while True:
      for direction in finger_direction(): #連続してdirectionを出してる
        for val in (direction or []): #Noneを止めう
          pass

          dir_list.append(direction)
          rs = sum([s.endswith('R') for s in dir_list])
          ls = sum([s.endswith('L') for s in dir_list])
  
          if len(dir_list)>30:
            dir_list.clear()

          if rs == 30 :
            print('右に向かいます')
            print('5秒後にカメラを閉じます')
            sleep(5)
            sys.exit()
          elif ls == 30:
            print('左に向かいます')
            print('5秒後にカメラを閉じます')
            sleep(5)
            sys.exit()
          else:
            print('...')
            
          
            
if  __name__ == '__main__':
   try:
     l_or_r()
   except rospy.ROSInterruptException: pass

#Pythonファイルが「python ファイル名.py というふうに実行されているかどうか」を判定するif文
#import hello した：hello.py 内部で __name__ は "hello" という文字列になる
# python hello.py した：hello.py 内部で __name__ は "__main__" という文字列になる
# =>[ __name__ == __main__]のとき、このファイルは**.py で直接実行される

