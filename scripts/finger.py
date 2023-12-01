#!/usr/bin/env python3
from hand_detect import finger_direction
from online_audio_kit import AudioKit
audio = AudioKit(language="ja")
import rospy
from std_msgs.msg import String
import time

r=0
l=0
count=50 #何回続いたらOKか（とりあえず１０）
rospy.init_node("finger_node",anonymous=True)
pub = rospy.Publisher("topic_direction", String, queue_size=1)
Direction ="None"

def right_or_left():
    global start
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
                    pub.publish(Direction)#方向をpublish
                        
                    break
                
            elif direction=="L":
                l=l+1
                r=0 #連続でない場合を除外
                print(r,l)#デバッグ

                if l>=count: #Rが１０回続いたとき
                    print("左方向です")
                    audio.tts("方向がわかりました。左方向ですね。")
                    Direction="left"
                    pub.publish(Direction)#方向をpublish
                    break  
            elif time.time()-start>=15:
                audio.tts("すみません、もう一度方向を教えてください") 
                start=time.time()
        
if __name__ == '__main__':
    try:
        print("fingerファイル読み込み")
        rospy.wait_for_message("topic_start_finger", String)
        print("方向開始")
        audio.tts("紙袋を持っている人の方向を指さして教えてください。")        
        rospy.loginfo("方向入力を開始します。")
        start=time.time()
        right_or_left()#デバッグ時コメントアウト
        #time.sleep(2)#テスト用
        #pub.publish("right") #テスト用
    except rospy.ROSInterruptException or KeyboardInterrupt:
        pass