#!/usr/bin/env python3
from online_audio_kit import AudioKit
import rospy
from std_msgs.msg import String
audio = AudioKit(language="ja")
#res=audio.stt()
#print(res)
rospy.init_node("audio_node")
pub = rospy.Publisher("topic_color", String, queue_size=1)
Color ="None"



def white_or_brown():
    for text in audio.vosk():
        if "白" in text:
            Color="white"
            print("白です")
            pub.publish(Color)#色をpublish
            break
        elif"茶色" in text:
            Color="brown"
            print("茶色です")
            pub.publish(Color)#色をpublish
            break
        else:
            continue

if __name__ == '__main__':
    while not rospy.is_shutdown():
        white_or_brown()
        break
    
    




