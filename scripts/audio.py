#!/usr/bin/env python3
from online_audio_kit import AudioKit
import rospy
import time
from std_msgs.msg import String
audio = AudioKit(language="ja")
rospy.init_node("audio_node",anonymous=True)
pub = rospy.Publisher("topic_color", String, queue_size=1)
Color ="None"



def white_or_brown():
    global Color

    while(1):
                text=audio.stt()
                if "白" in text:
                    Color="white"
                    audio.tts("紙袋の色がわかりました。しろ色ですね。")
                    print("白です")
                    pub.publish(Color)#色をpublish
                    break
                elif"茶色" in text:
                    Color="brown"
                    audio.tts("紙袋の色がわかりました。茶色ですね。")
                    print("茶色です")
                    pub.publish(Color)#色をpublish
                    break
                else:
                    audio.tts("もう一度お願いします")
                    continue


if __name__ == '__main__':
    try:
        print("audioファイル読み込み")
        rospy.wait_for_message("topic_start_audio", String)
        print("音声開始")
        audio.tts("紙袋の色を教えてください。白と茶色のどちらがいいですか？")
        rospy.loginfo("音声入力を開始します")
        #white_or_brown()#デバッグ時コメントアウト
        time.sleep(2)
        pub.publish("white") #テスト用

    except rospy.ROSInterruptException or KeyboardInterrupt:
        pass