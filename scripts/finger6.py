#!/usr/bin/env python3
from hand_detect import finger_direction
#import rospy
import sys

#   print(empty_list)
# if empty_list.count(empty_list[0]) == len(empty_list):
#   print(empty_list[0])

empty_list = []

# for direction in finger_direction():
while True:
  for direction in finger_direction():
    for val in (direction or []):
      pass #Noneをパス

      empty_list.append(direction)
      right = sum ([s.endswith('R') for s in empty_list]) #Rの合計個数
      left  = sum ([s.endswith('L') for s in empty_list]) #Lの合計個数

      #if len(empty_list)>20


      if right == 20:
        print("右です.")
        sys.exit()

      elif left == 20:
        print("左です.")
        sys.exit()

      else:
        print(empty_list)
        print("----")

# r ="R"
# l ="L"
# empty_list = []
# # len(empty_list) < 10
# for direction in finger_direction():
#   while len(empty_list) < 10:
#   # print(direction)
#         # if len(empty_list) < 10:print(empty_list)
  # if empty_list.count(empty_list[0]) == len(empty_list):
  #   print(empty_list[0])

#         #   empty_list.append(direction)
#         #   print(empty_list)
#     # if direction == "R":
#     empty_list.append(direction)
#     print(empty_list)
#     # r = r + 1