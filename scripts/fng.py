#!/usr/bin/env python3
from std_msgs.msg import String
import rospy
from hand_detect import finger_direction

for direction in finger_direction():
  print(direction)