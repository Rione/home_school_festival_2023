#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from hand_detect import finger_direction

# Configurable variables
limit: int = 10     # How many times to receive data from hand_detect

def CreateFingerDirectionNode() -> None:
    # Node and publisher
    pub = rospy.Publisher('topic_direction', String, queue_size=1)
    rospy.init_node('finger_node', anonymous=True)

    # Initialization
    counter_L = 0
    counter_R = 0

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

    rospy.loginfo(f"[Debug] Set direction to: {result}")
    pub.publish(result) # Publish a topic regardless of the subscriber already established or not

if __name__ == '__main__':
    try:
        CreateFingerDirectionNode()
    except rospy.ROSInterruptException:
        pass
