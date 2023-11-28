#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import String
from online_audio_kit import AudioKit
audio = AudioKit(language="ja")
rospy.init_node("main_node",anonymous=True)
pub_audio = rospy.Publisher("topic_start_audio", String, queue_size=1)
pub_finger = rospy.Publisher("topic_start_finger", String, queue_size=1)
pub_send_goal=rospy.Publisher("topic_move", String, queue_size=1)
rospy.Subscriber("topic_color",String,)
rospy.Subscriber("topic_direction",String,)
rospy.Subscriber("topic_fin",String,)
PUB="***" #なんでもいい


def res_check():
    while(1):
    #    res=audio.stt()#紙袋受け渡し/受け取り確認
    #    if "OK" in res:
            break

if __name__ == '__main__':
    try:
        for i in range(10):
            pub_audio.publish(PUB)#audio起動
            time.sleep(0.1)

        Color=rospy.wait_for_message("topic_color", String)#audio終了まで待機

        for i in range(10):
            pub_finger.publish(PUB)#finger起動
            time.sleep(0.1)
        target=rospy.wait_for_message("topic_direction", String)#finger終了まで待機
        print("色と方向がわかりました")
        print(Color,target)
        
        if Color.data=="white":
            Color="しろ色"
        elif Color.data=="brown":
            Color="茶色"


        if  target=="right":#１回目移動目標設定
            target="target1"
        else:
            target="target2"
        for i in range(1):
            pub_send_goal.publish(target)#移動１回目起動
            time.sleep(0.1)

        rospy.wait_for_message("topic_fin", String)#移動１回目終了まで待機
        print("finトピック受信")

        audio.tts(f"{Color}の紙袋をください")

        res_check()#紙袋受け渡し確認
        
        if  target=="target1":#２回目移動目標設定
            target="target2"
        else:
            target="target1"
        
        for i in range(1):
            pub_send_goal.publish(target)#移動２回目起動
            time.sleep(0.1)
        rospy.wait_for_message("topic_fin", String)#移動２回目終了まで待機

        audio.tts(f"{Color}の紙袋を持ってきました")
        
        res_check()#紙袋受け取り確認

        for i in range(1):
            pub_send_goal.publish("origin")#移動３回目起動
            time.sleep(0.1)
        
        
    except rospy.ROSInterruptException or KeyboardInterrupt:
        pass