#!/usr/bin/env python3
from online_audio_kit import AudioKit
from std_msgs.msg import String
import rospy
audio = AudioKit(language = 'ja')
# global Col
Col = "none"

class AudioKit():

  def __init__(self):
    self.pub = rospy.Publisher("topic_color", String, queue_size=10)

  #def publish(self):
    #audio.tts("紙袋の色を教えてください")
    while True:
      # for text in audio.vosk():
        text = audio.stt()
        if '白' in text:
          Col = "white"
          print('白です')
          self.pub.publish(Col)
          break
        elif '茶色' in text:
          Col = "brown"
          print('茶色です')
          self.pub.publish(Col)
          break
        # else:
        #   audio.stt()
        #   continue
      
      #self.pub.publish(Color)

if __name__ == "__main__":
  
  rospy.init_node("audio_node")
  
  audio = AudioKit()
  
  rate = rospy.Rate(1)

  while not rospy.is_shutdown():
    #publish
    audio.publish()
        
    rate.sleep()