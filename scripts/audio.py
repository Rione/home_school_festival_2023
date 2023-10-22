#!/usr/bin/env python3
from online_audio_kit import AudioKit
import rospy
from std_msgs.msg import String
audio = AudioKit(language="ja")
#res=audio.stt()
#print(res)
rospy.init_node("audio")
pub = rospy.Publisher("color", String, queue_size=1)
Color ="None"

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