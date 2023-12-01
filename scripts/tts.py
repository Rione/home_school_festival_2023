#!/usr/bin/env python3

ENV_PATH = ""

import rospy
import os
from dotenv import load_dotenv
from std_msgs.msg import String
from playsound import playsound


rospy.init_node('tts_node', anonymous=True)

load_dotenv(dotenv_path=ENV_PATH)

def TextToSpeech(data) -> None:
    rospy.loginfo("[Debug] tts called.")
    prefix = os.getenv('VOICE_PATH')
    try:
        playsound(prefix + data.data + '.mp3')
    except Exception as e:
        rospy.loginfo(f"[Error] Exception occurred: {e}")

    return

def main():
    rospy.Subscriber("topic_tts", String, TextToSpeech)
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
