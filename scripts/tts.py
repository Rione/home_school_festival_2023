#!/usr/bin/env python3

ENV_PATH = "/home/yuko001/catkin_ws/src/home_school_festival_2023/.env"

import rospy
import os
from dotenv import load_dotenv
from std_msgs.msg import String
from playsound import playsound


load_dotenv(dotenv_path=ENV_PATH)

def TextToSpeech(data) -> None:
    rospy.loginfo("[Debug] tts called.")
    prefix = os.getenv('VOICE_PATH')
    try:
        playsound(prefix + data.data + '.mp3')
    except Exception as e:
        rospy.loginfo(f"[Error] Exception occurred: {e}")

    return

if __name__ == "__main__":
    try:
        rospy.init_node('tts_node', anonymous=True)
        rospy.Subscriber("topic_tts", String, TextToSpeech)
        print("tts_node: ready")
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
