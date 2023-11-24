#!/usr/bin/env python3

import rospy
import actionlib
import numpy as np
from std_msgs.msg import String
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


GOAL_POS = [
    [0, 0, 0],  # Origin
    [0, 0, 0],  # Target1
    [0, 0, 0],  # Target2
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

def MoveToTarget(data, pub):
    rospy.loginfo(f"[Debug] The target is {data.data}.")

    if(data.data == 'origin'):
        target_pos = GOAL_POS[0]
    elif(data.data == 'target1'):
        target_pos = GOAL_POS[1]
    elif(data.data == 'target2'):
        target_pos = GOAL_POS[2]

    rospy.loginfo(f"[Info] Moving to {target_pos}.")
    # Wait for the navigation to finish
    result = move_base_client(target_pos[0], target_pos[1], target_pos[2])
    rospy.loginfo(f"[Debug] result: {result}")
    pub.publish(result)

def CreateSendGoalNode():
    rospy.init_node("send_goal_node", anonymous=True)
    pub = rospy.Publisher('topic_end_nav', String, queue_size=1)
    rospy.Subscriber("topic_move", String, MoveToTarget, pub)
    rospy.spin()

if __name__ == "__main__":
    try:
        CreateSendGoalNode()
    except rospy.ROSInterruptException:
        pass