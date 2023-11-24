#!/usr/bin/env python3
from std_msgs.msg import String
import rospy
from hand_detect import finger_direction

# args : camera_id (default: 0)
# yield : direction ("R" | "L" | None)
# ESC to exit
Dir = "none"
class Finger():

    def __init__(self):
        self.pub = rospy.Publisher("topic_direction", String, queue_size=10)

        R = 0
        R = 0
        for direction in finger_direction():
            #print(direction)

            if  direction == "R":
                R += 1
                L = 0
            elif direction == "L":
                L += 1
                R = 0
            
            if R >= 10:
                Dir = "right"
                self.pub.publish(Dir)
                break

            elif R >= 10:
                Dir = "left"
                self.pub.publish(Dir)
                break

if __name__ == "__main__":

    rospy.init_node("finger_node")
    
    finger = Finger()
    
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # パブリッシュ
        finger.publish()
        
        rate.sleep()