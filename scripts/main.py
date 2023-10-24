#!/usr/bin/env python3
import rospy
import time
from Controller import Controller

def main():
    # Create an instance
    ctrl = Controller()

    ctrl.ListenToBagColor()
    ctrl.ListenToDirection()
    rospy.loginfo('Listening to audio_processing and finger_direction.')

    # Wait for both color and direction to be specified
    while(ctrl.bagColor == None or ctrl.direction == None):
        time.sleep(0.1)

    #----WIP-------------------------------------
    

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        rospy.logerr("An exception has been occurred during the execution.")