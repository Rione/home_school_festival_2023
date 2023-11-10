#!/usr/bin/env python3
from online_audio_kit import AudioKit
from gtts import gTTS
import time
import rospy
from std_msgs.msg import String

audio = AudioKit(language= "ja")


def brown_or_white():
    rospy.Publisher('topic_color', String, queue_size=10) #topicは情報の名前 pub=(topic)=>lis
    rospy.init_node('audio_node', anonymous=True) #finger_nodeはpublisherのノード　pub=>lis
    r = rospy.Rate(10) # 10hz
    
    n=0
    for text in audio.vosk():
        if text == '茶色':
          print('茶色')
          break
        elif text == '白':
          print('白')
          break
        else:
          time.sleep(15)
          print('もう一度')
          n +=1
          if n==5:
            break
      
if  __name__ == '__main__':
  try:
    brown_or_white()
  except rospy.ROSInterruptException: pass  

      
 