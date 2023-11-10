#!/usr/bin/env python3
from online_audio_kit import AudioKit
from std_msgs.msg import String
import rospy
audio = AudioKit(language = 'ja')

class AudioKit():

  def __init__(self):
    self.pub = rospy.Publisher("topic_color", String, queue_size=10)

  #def publish(self):
    shiro = '白'
    cha   = '茶色'
    for text in audio.vosk():
      if shiro in text:
        print('しろです')
        break
      elif cha in text:
          print('ちゃいろです')
          break
      
      self.pub.publish()

if __name__ == "__main__":
  
  rospy.init_node("audio_node")
  
  
  audio = AudioKit()
  
  rate = rospy.Rate(1)

  while not rospy.is_shutdown():
    # パブリッシュ
    audio.publish()
        
    rate.sleep()