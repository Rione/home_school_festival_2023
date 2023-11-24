#!/usr/bin/env python3
from hand_detect import finger_direction
import rospy
import sys
# args : camera_id (default: 0)
# yield : direction ("R" | "L" | None)
# Edef __init__(self):SC to exit

while True:
  for direction in finger_direction():
      class Finger():
        r = 0
        l = 0
        def __init__(self):
          self.pub = rospy.Publisher("topic_direction", String, queue_size=10)
        #print(direction)
          if direction  == "R":
            r += 1
            
          if r > 10:
                self.pub.publish("right")
                break
            
          elif direction  == "L":
            l += 1
          if l > 10:
                self.pub.publish("left")
                break

if __name__ == "__main__":

    rospy.init_node("finger_node")
    
    finger = Finger()
    
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # パブリッシュ
        finger.publish()
        
        rate.sleep()





    