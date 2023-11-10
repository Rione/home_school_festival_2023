#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
result_color=None
result_direction=None

def main():
    rospy.Subscriber('topic_direction', String, finger) #topicは情報の名前 pub=(topic)=>lis
    rospy.Subscriber('topic_color', String, audio) #topicは情報の名前 pub=(topic)=>lis
    rospy.init_node('main_node', anonymous=True) #finger_nodeはpublisherのノード　pub=>lis
    rospy.spin()
    
def finger(direction):
    if direction.data =='R':
        direction==True
    if direction.data =='L':
        result_direction==True
    
def audio(color):
    if color.data =='R':
        color==True
    if color.data =='白':
        result_color==True


while result_color != True and result_direction != True:

 if  __name__ == '__main__':
   try:
     main()
   except rospy.ROSInterruptException: pass
else:
    print('出発します')
    