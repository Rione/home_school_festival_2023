#!/usr/bin/env python3

ENV_PATH = ""

import rospy
import actionlib
import numpy as np
import os
from dotenv import load_dotenv
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


load_dotenv(dotenv_path=ENV_PATH)
GOAL_POS = [
    [os.getenv("ORIGIN_X"), os.getenv("ORIGIN_Y"), os.getenv("ORIGIN_Z") ],  # Origin
    [os.getenv("TARGET1_X"), os.getenv("TARGET1_Y"), os.getenv("TARGET1_Z") ],  # Target1
    [os.getenv("TARGET2_X"), os.getenv("TARGET2_Y"), os.getenv("TARGET2_Z") ],  # Target2
]

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

def MoveToTarget(data):
    target = data.data
    rospy.loginfo(f"[Debug] The target is {target}.")

    if(target == 'origin'):
        target_pos = GOAL_POS[0]
    elif(target == 'target1'):
        target_pos = GOAL_POS[1]
    elif(target == 'target2'):
        target_pos = GOAL_POS[2]

    rospy.loginfo(f"[Info] Moving to {target_pos}.")
    # Wait for the navigation to finish
    result = str(move_base_client(target_pos[0], target_pos[1], target_pos[2]))
    rospy.loginfo(f"[Debug] result: {result}")
    pub_nav_fin.publish(result)

    return

if __name__ == "__main__":
    try:
        rospy.init_node("send_goal_node", anonymous=True)
        pub_nav_fin = rospy.Publisher('topic_nav_finished', String, queue_size=1)
        rospy.Subscriber("topic_move", String, MoveToTarget)
        print("send_goal_node: ready")
        rospy.spin()
    except rospy.ROSInterruptException:
        pass