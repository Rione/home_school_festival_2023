#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import String
from hand_detect import finger_direction

# Configurable variables
limit: int = 10     # How many times to receive data from hand_detect

def CreateFingerDirectionNode() -> None:
    # Node and publisher
    pub_direction = rospy.Publisher('topic_direction', String, queue_size=1)
    pub_tts = rospy.Publisher('topic_tts', String, queue_size=1)
    rospy.init_node('finger_node', anonymous=True)

    # Initialization
    counter_L = 0
    counter_R = 0

    pub_tts("行きたい方向を指してください。")
    time.sleep(3)

    # Main
    for direction in finger_direction():
        # args : camera_id (default: 0)
        # yield : direction ("R" | "L" | None)
        # ESC to exit
        if(direction):
            if(direction == 'L'):
                counter_R = 0
                counter_L += 1
            elif(direction == 'R'):
                counter_L = 0
                counter_R += 1

            if(counter_L >= limit):
                result =  'left'
                break
            elif(counter_R >= limit):
                result =  'right'
                break
        else: # Reset counters
            counter_L = 0
            counter_R = 0

    rospy.logdebug(f"[Debug] Set direction to: {result}")
    pub_tts("わかりました。")
    time.sleep(3)
    pub_direction.publish(result) # Publish a topic regardless of the subscriber already established or not

if __name__ == '__main__':
    try:
        CreateFingerDirectionNode()
    except rospy.ROSInterruptException:
        pass

