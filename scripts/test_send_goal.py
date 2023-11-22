#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
import time
import numpy as np


GOAL_POS=[0,0,0]

rospy.init_node("send_goal_node")
#change here
def set_goal(target):
    print(target.data)
    global GOAL_POS
    global start
    if(target.data=="target1"):
        GOAL_POS = [1,1,1]
    elif(target.data=="target2"):
        GOAL_POS = [2,2,2]
    elif(target.data=="origin"):
        GOAL_POS = [3,3,3]
    else:
        GOAL_POS = [0 ,0, 0]

    print(GOAL_POS)
    #result = move_base_client(GOAL_POS[0], GOAL_POS[1], GOAL_POS[2])
    print(f"{target}が終わりました")
    #rospy.loginfo(result)




    



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
    
    sub=rospy.Subscriber("topic_move",String,set_goal)
    rospy.spin()




        

