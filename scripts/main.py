#!/usr/bin/env python3
from online_audio_kit import AudioKit
from std_msgs.msg import String
from hand_detect import finger_direction
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import rospy

#audio = AudioKit(language="ja")

class AudioKit_Finger():
    # audio.tts("紙袋の色を教えてください")
    def __init__(self):
        self.sub = rospy.Subscriber("topic_color", String, self.call_color)
        self.sub = rospy.Subscriber("topic_direction", String, self.call_dir)
        self.addint_srv = rospy.Service("topic_move", MoveBaseAction, self.call_loc)

    def call_color(self,data):
        if "white" or "brown" in self.sub:
            rospy.loginfo("色を取得しました")

    def call_dir(self,data):
        if "right" or "left" in self.sub.direction.Dir:
            rospy.loginfo("方向を取得しました")
        # else:
        #     audio.stt("もう一度お願いします")

        # if "白" in self.sub.String:
        #     rospy.loginfo("白色を取得しました")

        # elif "茶色" in self.sub.String:
        #     rospy.loginfo("茶色を取得しました")
        

if __name__ == "__main__":
    rospy.init_node("main_node")

    audiokit_finger = AudioKit_Finger()
    # Ctrl-Cまで
    rospy.spin()
