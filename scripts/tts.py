#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from playsound import playsound


def TextToSpeech(data) -> None:
    rospy.loginfo("[Debug] tts called.")
    filename = data.data
    path = "/root/catkin_ws/src/home_school_festival_2023/voice/" + filename + ".mp3"
    try:
        playsound(path)
    except Exception as e:
        rospy.loginfo(f"[Error] Exception occurred: {e}")
    pub_tts_fin.publish("wait")

    return

if __name__ == "__main__":
    try:
        rospy.init_node('tts_node', anonymous=True)
        pub_tts_fin = rospy.Publisher('topic_tts_finished', String, queue_size=1)
        rospy.Subscriber("topic_tts", String, TextToSpeech)
        print("tts_node: ready")
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
