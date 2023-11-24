#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import String
from hand_detect import finger_direction


def CreateFingerDirectionNode() -> None:
    # Node and publisher
    rospy.init_node('finger_node', anonymous=True)
    pub_dir = rospy.Publisher('topic_direction', String, queue_size=1)
    pub_tts = rospy.Publisher('topic_tts', String, queue_size=1)

    pub_tts.publish("ask_direction")
    time.sleep(3)   # Wait for the audio to stop

    limit: int = 10     # How many times to receive data from hand_detect

    counter_L = 0
    counter_R = 0
    result = None
    rospy.loginfo("[Info] Press ESC to exit.")
    # args : camera_id (default: 0)
    # yield : direction ("R" | "L" | None)
    # ESC to exit
    for direction in finger_direction():
        if(direction):
            if(direction == 'L'):
                counter_R = 0
                counter_L += 1
                if(counter_L >= limit):
                    result =  'left'
                    break
            elif(direction == 'R'):
                counter_L = 0
                counter_R += 1
                if(counter_R >= limit):
                    result =  'right'
                    break             
        else: # Reset counters
            counter_L = 0
            counter_R = 0

    rospy.loginfo(f"[Debug] Set direction to: {result}")

    if(result != None):
        pub_dir.publish(result) # Publish a topic without waiting for the subscriber being established
    else: rospy.loginfo("[Error] The direction is not given. Please try again.")

if __name__ == '__main__':
    try:
        CreateFingerDirectionNode()
    except rospy.ROSInterruptException:
        pass

