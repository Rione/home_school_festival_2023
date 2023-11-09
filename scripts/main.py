#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
rospy.init_node("main_node")
direction_fin=False
color_fin=False


def dir(direction):
  print("方向を受信しました")
  print(direction)
  global direction_fin

  if direction.data=="right":
    direction_fin=True

  elif direction.data=="left":
    direction_fin=True


def col(color):
  global color_fin
  print("色を受信しました")
  print(color)
  if color.data=="brown":
    print("brown")
    color_fin=True

  elif color.data=="white":
    print("white")
    color_fin=True

while not rospy.is_shutdown():
  sub=rospy.Subscriber("topic_direction",String,dir)
  sub=rospy.Subscriber("topic_color",String,col)
  if (direction_fin==True and color_fin==True):
    break
print("色と方向がわかりました")   

  

  