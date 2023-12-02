#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import String
from std_srvs.srv import SetBool, SetBoolResponse
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

def AskFingerDirection(_) -> None:
    resp = SetBoolResponse()

    pub_tts.publish("ask_direction")
    time.sleep(3)

    result = DetectFingerDirection(limit=50)
    if(result == 'left'):
        resp.message = "left"
    elif(result == 'right'):
        resp.message = "right"
    time.sleep(1)

    resp.success = True
    rospy.loginfo(f"[Debug] Set direction to: {resp.message}")

    return resp

if __name__ == '__main__':
    try:
        rospy.init_node('finger_node', anonymous=True)
        pub_tts = rospy.Publisher('topic_tts', String, queue_size=1)
        srv = rospy.Service('srv_init_camera', SetBool, AskFingerDirection)
        print('finger_node: ready')
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

