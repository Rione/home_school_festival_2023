#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import String
from online_audio_kit import AudioKit
audio = AudioKit(language="ja")
rospy.init_node("test_node")
direction_fin=False
color_fin=False
goal_fin=False
#pub = rospy.Publisher("audio_and_finger", String, queue_size=1)
start = time.time()
target="None"
Color="None"

def dir(direction):
  global direction_fin
  global target

  if direction_fin==False:
    print("方向を受信しました")
    print(direction)

    if direction.data=="right":
      direction_fin=True
      target="target1"
      audio.tts("方向がわかりました。右方向ですね。")
      
      

    elif direction.data=="left":
      direction_fin=True
      target="target2"
      audio.tts("方向がわかりました。左方向ですね。")
      
      


def col(color):
  global color_fin
  global Color
  if color_fin==False:
    print("色を受信しました")
    print(color)

    if color.data=="brown":
      color_fin=True
      Color="茶"
      audio.tts("紙袋の色がわかりました。茶色ですね。")
      
      

    elif color.data=="white":
      color_fin=True
      Color="しろ"
      audio.tts("紙袋の色がわかりました。しろ色ですね。")
      
      



if __name__ == '__main__':
      audio.tts("紙袋の色と荷物を持っている人の方向を教えてください。")
      while not rospy.is_shutdown():
        try:
            if (direction_fin==False):
                rospy.Subscriber("topic_direction",String,dir)
            if (color_fin==False):
                rospy.Subscriber("topic_color",String,col)
            if (direction_fin==True and color_fin==True):
                print("色と方向がわかりました")
                break
            if (time.time()-start>=15 ):
                if(direction_fin==False):
                    if(color_fin==False):
                      audio.tts("すみません、色と方向をもう一度教えてください")
                      start = time.time()
                    else:
                      audio.tts("すみません、人の方向をもう一度教えてください")
                      start = time.time()
                elif(color_fin==False):
                    audio.tts("すみません、紙袋の色をもう一度教えてください")
                    start = time.time()

        except rospy.ROSInterruptException or KeyboardInterrupt:
            pass




#rospy.init_node("main_node")





pub = rospy.Publisher("topic_move", String, queue_size=1)



#audio_and_finger.py からturget & color情報取得

print(Color,target)




target="target1"

pub.publish(target)
time.sleep(10)
audio.tts(f"{Color}の紙袋をください")

while(1):
    res=audio.stt()
    if "OK" in res:
      break


if target=="target1":
  target="target2"
else:
  target="taeget1"

pub.publish(target)
time.sleep(10)
audio.tts(f"{Color}の紙袋を持ってきました")

while(1):
  res=audio.stt()
  if "OK" in res:
    break

pub.publish("origin")


