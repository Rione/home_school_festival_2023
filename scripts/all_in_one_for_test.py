#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from online_audio_kit import AudioKit
audio = AudioKit(language="ja")
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from hand_detect import finger_direction

import time
import numpy as np

rospy.init_node("send_goal_node")
GOAL_POS = [0,0, 0]
r=0
l=0
count=50 #何回続いたらOKか（とりあえず１０）
Target1=(-0.28,-0.83,0.002)#右の人
Target2=(-1.5,-1.8,0.002)#左の人
Origin=(-1.23,-0.38,0.002)#もといた場所


def change_goal(a,b,c):
    global GOAL_POS
    GOAL_POS = [a,b,c]

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

def send_goal():
    print(f"{GOAL_POS[0], GOAL_POS[1], GOAL_POS[2]}に移動します")
    time.sleep(2)

    result = move_base_client(GOAL_POS[0], GOAL_POS[1], GOAL_POS[2])
    rospy.loginfo(result)


def finger():
    start=time.time()
    audio.tts("方向を指さして教えてください。")
    global r
    global l
    for direction in finger_direction():
            print(direction)
            
            if direction=="R":

                r=r+1
                l=0 #連続でない場合を除外
                print(r,l)#デバッグ

                if r>=count: #Rが１０回続いたとき
                    print("右方向です")
                    audio.tts("方向がわかりました。右方向ですね。")
                    Direction="right"    
                    break
                
            elif direction=="L":
                l=l+1
                r=0 #連続でない場合を除外
                print(r,l)#デバッグ

                if l>=count: #Rが１０回続いたとき
                    print("左方向です")
                    audio.tts("方向がわかりました。左方向ですね。")
                    Direction="left"

                    break  
            elif start-time.time()>=15:
                audio.tts("すみません、もう一度方向を教えてください") 
                start=time.time()
    return(Direction)

def Audio():
    audio.tts("紙袋の色を教えてください。しろ色がいいですか、茶色がいいですか")

    while(1):
                text=audio.stt()
                if "白" in text:
                    Color="しろ色"
                    audio.tts("紙袋の色がわかりました。しろ色ですね。")
                    print("白です")
                    break
                elif"茶色" in text:
                    Color="茶色"
                    audio.tts("紙袋の色がわかりました。茶色ですね。")
                    print("茶色です")
                    break
                else:
                    audio.tts("もう一度お願いします")
                    continue
    return(Color)

if __name__ == '__main__':
    try:
        Color=Audio()
        target=finger()
        #Color="しろ"#デバッグ用
        #target="left"#デバッグ用

        print("色と方向がわかりました")
        audio.tts("移動を開始します。")

        if  target=="right":
            change_goal(*Target1)
        else:
            change_goal(*Target2)
        

        send_goal()

        audio.tts(f"{Color}の紙袋をアームに掛けてください")

        
        
        while(1):
            audio.tts("受け渡しは終わりましたか")
            res=audio.stt()
            if "はい" in res:
                break
        audio.tts("わかりました。ありがとうございます。")
        
        if  target=="right":
            change_goal(*Target2)
        else:
            change_goal(*Target1)

        send_goal()

        audio.tts(f"{Color}の紙袋を持ってきました")
        
        while(1):
            audio.tts("紙袋を受け取りましたか")
            res=audio.stt()
            if "はい" in res:
                break
        audio.tts("元の場所に戻ります")
        change_goal(*Origin)
        send_goal()
        
    except rospy.ROSInterruptException or KeyboardInterrupt:
        pass







