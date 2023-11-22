##!/usr/bin/env python3
#from hand_detect import finger_direction
#from online_audio_kit import AudioKit
#import rospy
#from std_msgs.msg import String
#import time
##rate = rospy.Rate(10)
## args : camera_id (default: 0)
## yield : direction ("R" | "L" | None)
## ESC to exit
#r=0
#l=0
#count=10 #何回続いたらOKか（とりあえず１０）
##rospy.init_node("finger_node")
#pub = rospy.Publisher("topic_direction", String, queue_size=1)
#Direction ="None"
#
#def right_or_left():
#    global r
#    global l
#    for direction in finger_direction():
#            print(direction)
#            
#            if direction=="R":
#
#                r=r+1
#                l=0 #連続でない場合を除外
#                print(r,l)#デバッグ
#
#                if r>=count: #Rが１０回続いたとき
#                    print("右方向です")
#                    Direction="right"
#                    pub.publish(Direction)#方向をpublish
#                        
#                    break
#                
#            elif direction=="L":
#                l=l+1
#                r=0 #連続でない場合を除外
#                print(r,l)#デバッグ
#
#                if l>=count: #Rが１０回続いたとき
#                    print("左方向です")
#                    Direction="left"
#                    pub.publish(Direction)#方向をpublish
#                    break   
#        
#if __name__ == '__main__':
#    try:
#        time.sleep(8)
#        rospy.loginfo("方向入力を開始します。")
#        right_or_left()
#    except rospy.ROSInterruptException or KeyboardInterrupt:
#        pass
#
#

        

