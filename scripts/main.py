#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
rospy.init_node("main_node")
direction_fin=False
color_fin=False


def dir(direction):
  global direction_fin
  if direction_fin==False:
    print("方向を受信しました")
    print(direction)
  

  if direction.data=="right":

    direction_fin=True

  elif direction.data=="left":

    direction_fin=True



def col(color):
  global color_fin
  if color_fin==False:
    print("色を受信しました")
    print(color)
  if color.data=="brown":
    color_fin=True

  elif color.data=="white":
    color_fin=True



if __name__ == '__main__':
    while not rospy.is_shutdown():
      try:
          if (direction_fin==False):
              rospy.Subscriber("topic_direction",String,dir)
          if (color_fin==False):
              rospy.Subscriber("topic_color",String,col)
          if (direction_fin==True and color_fin==True):
              print("色と方向がわかりました")
              break
      except rospy.ROSInterruptException:
            pass
  

  