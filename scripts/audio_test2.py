#!/usr/bin/env python3
from online_audio_kit import AudioKit
from std_msgs.msg import String
import rospy

audio = AudioKit(language = 'ja')
rospy.init_node("audio_node")
pub = rospy.Publisher("topic_color", String, queue_size=10)
Color="None"

class AudioKit():

  def white_or_brown():
    audio.tts("紙袋の色を教えてください")
    while(True):
      text=audio.stt()
      color= String()
      shiro = '白'
      cha   = '茶色'
      #for text in audio.vosk():
      if shiro in text:
        Color = "white"
        print('しろです')
        pub.publish(Color)
        break
      elif cha in text:
        Color = "brown"
        print('ちゃいろです')
        pub.publish(Color)
        break
      else:
        print("...") 
        audio.tts("もう一度お願いします") 
        continue   

if __name__ == "__main__":
  
  audio = AudioKit()
  
  rate = rospy.Rate(1)

  while not rospy.is_shutdown():
    # パブリッシュ
    audio.publish(Color)
        
    rate.sleep()