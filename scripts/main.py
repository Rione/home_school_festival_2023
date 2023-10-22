#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def main() -> None:
    rospy.init_node('controller', anonymous=True)
    rospy.Subscriber("finger_direction", String, FingerDirectionCallback)

    rospy.spin()

