#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
import time
import numpy as np
start=False
fin = rospy.Publisher("topic_fin", String, queue_size=1)



# change here
def set_goal(target):
    global GOAL_POS
    global start
    if(target=="target1"):
        GOAL_POS = [-0.9911009073257446, -0.2397373616695404, 0]
    elif(target=="target2"):
        GOAL_POS = [-0.9911009073257446, -0.2397373616695404, 0]
    elif(target=="origin"):
        GOAL_POS = [-0.9911009073257446, -0.2397373616695404, 0]
    else:
        GOAL_POS = [0 ,0, 0]

    



def move_base_client(x, y, yaw):
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id= "map"
    goal.target_pose.header.stamp= rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = 0
    goal.target_pose.pose.orientation.x = 0
    goal.target_pose.pose.orientation.y = 0
    goal.target_pose.pose.orientation.z = np.sin(yaw / 2)
    goal.target_pose.pose.orientation.w = np.cos(yaw / 2)

    client.send_goal(goal)

    client.wait_for_result()

    return client.get_result()




if __name__ == "__main__":
    while(1):
        #while(1):
        #    sub=rospy.Subscriber("topic_move",String,set_goal)
        #    if(GOAL_POS!=[0,0,0]):
        #        break


        rospy.init_node("send_goal_node")
        time.sleep(2)
        result = move_base_client(GOAL_POS[0], GOAL_POS[1], GOAL_POS[2])
        rospy.loginfo(result)
        rospy.spin()

