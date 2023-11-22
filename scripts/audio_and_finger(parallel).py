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
      audio.tts("方向がわかりました。右方向ですね。")
      target="target1"
      direction_fin=True

    elif direction.data=="left":
      audio.tts("方向がわかりました。左方向ですね。")
      target="target2"
      direction_fin=True


def col(color):
  global color_fin
  global Color
  if color_fin==False:
    print("色を受信しました")
    print(color)

    if color.data=="brown":
      audio.tts("紙袋の色がわかりました。茶色ですね。")
      Color="茶"
      color_fin=True

    elif color.data=="white":
      audio.tts("紙袋の色がわかりました。しろ色ですね。")
      Color="しろ"
      color_fin=True


def main():
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
  return(Color,target)


