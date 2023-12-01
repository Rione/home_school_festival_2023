#!/usr/bin/env python3

import rospy
import env
from std_msgs.msg import String
from playsound import playsound


def TextToSpeech(data) -> None:
    rospy.loginfo("[Debug] tts called.")
    prefix = env.VOICE_PATH
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
