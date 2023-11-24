#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
import numpy as np
import time
PUB="***"


GOAL_POS=[0,0,0]#初期化
Target1=[-2.9,0.135,0.002]#右の人
Target2=[0.617,-0.271,0.002]#左の人
Origin=[0.220,0.715,0.002]#もといた場所

rospy.init_node("test_send_goal_node",anonymous=True)
pub=rospy.Publisher("topic_fin", String, queue_size=1)
#change here
def set_goal(target):#受け取ったトピックに合わせて目標設定
    global GOAL_POS
    if(target.data=="target1"):
        GOAL_POS = Target1
    elif(target.data=="target2"):
        GOAL_POS = Target2
    elif(target.data=="origin"):
        GOAL_POS = Origin
    else:
        GOAL_POS = [0 ,0, 0]

    print(GOAL_POS)
    print(f"{target}を開始します")
    print(f"{GOAL_POS[0], GOAL_POS[1], GOAL_POS[2]}に移動します")
    result = move_base_client(GOAL_POS[0], GOAL_POS[1], GOAL_POS[2])#デバッグ時コメントアウト
    rospy.loginfo(result)#デバッグ時コメントアウト
    rospy.spin()
    
    
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
        n=0
        rospy.wait_for_message("topic_move", String)
        sub=rospy.Subscriber("topic_move",String,set_goal)

        print("fin送信")
        for i in range(10):
            pub.publish(PUB)
            time.sleep(0.1)
        if n>=3:
            break
        n+=1
        
        

    
    




        

