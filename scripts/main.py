#!/usr/bin/env python3
import rospy
import time
from Controller import Controller

def main() -> None:
    ctrl = Controller()

    ctrl.setBagColor()
    ctrl.setDirection()
    rospy.loginfo('>> Listening to the color and direction.')

    # Wait for both color and direction
    while(ctrl.bagColor == None or ctrl.direction == None):
        time.sleep(0.1)

    #----WIP-------------------------------------
    

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass