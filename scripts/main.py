#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import String
from online_audio_kit import AudioKit
from audio_and_finger import main
audio = AudioKit(language="ja")
rospy.init_node("main_node")
pub = rospy.Publisher("topic_move", String, queue_size=1)

start = time.time()

#audio_and_finger.py からturget & color情報取得

color,target=main()



pub.pubulish(target)

audio.tts(f"{color}の紙袋をください")

while(1):
  res=audio.stt()
  if "OK" in res:
    break


if target=="target1":
  target="target2"
else:
  target="taeget2"


pub.pubulish(target)



audio.tts(f"{color}の紙袋を持ってきました")

while(1):
  res=audio.stt()
  if "OK" in res:
    break


pub.pubulish("origin")


