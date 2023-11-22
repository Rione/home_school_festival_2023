##!/usr/bin/env python3
#from online_audio_kit import AudioKit
#import rospy
#from std_msgs.msg import String
#import time
#audio = AudioKit(language="ja")
#
##rospy.init_node("audio_node")
#pub = rospy.Publisher("topic_color", String, queue_size=1)
#Color ="None"
#
#
#
#def white_or_brown():
#    global Color
#
#    while(1):
#                text=audio.stt()
#                if "白" in text:
#                    Color="white"
#                    print("白です")
#                    pub.publish(Color)#色をpublish
#                    break
#                elif"茶色" in text:
#                    Color="brown"
#                    print("茶色です")
#                    pub.publish(Color)#色をpublish
#                    break
#                # else:
#                #     audio.tts("もう一度お願いします")
#                #     continue
#
#
#if __name__ == '__main__':
#    try:
#        time.sleep(8)
#        rospy.loginfo("音声入力を開始します")
#        white_or_brown()
#
#    except rospy.ROSInterruptException or KeyboardInterrupt:
#        pass
#
#



