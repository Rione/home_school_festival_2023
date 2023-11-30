#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import String
from hand_detect import finger_direction


def DetectFingerDirection(limit:int) -> str:
    counter_L = 0
    counter_R = 0
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
    
    return result

def CreateFingerDirectionNode() -> None:
    # Node and publisher
    rospy.init_node('finger_node', anonymous=True)
    pub_dir = rospy.Publisher('topic_direction', String, queue_size=1)
    pub_audio = rospy.Publisher('topic_audio', String, queue_size=1)

    pub_audio.publish("ask_direction")
    time.sleep(3)   # Wait for the audio to stop

    boolean:str = 'no'
    while(boolean == 'no'):
        result = DetectFingerDirection(limit=50)
        pub_audio.publish('start_yes')
        boolean = rospy.wait_for_message('topic_end_yes', String, timeout=None)

    rospy.loginfo(f"[Debug] Set direction to: {result}")

    try:
        pub_dir.publish(result) # Publish a topic without waiting for the subscriber being established
    except Exception as e: 
        rospy.loginfo(f"[Error] Exception occurred: {e}")

    return

def main() -> None:
    rospy.Subscriber("topic_camera", String, CreateFingerDirectionNode)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

