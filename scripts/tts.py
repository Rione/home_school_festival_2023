#!/usr/bin/env python3

import rospy
import env
import time
from std_msgs.msg import String
from playsound import playsound
from mutagen.mp3 import MP3


def GetDurationOfMP3(path) -> int:
    audio = MP3(path)
    return audio.info.length

def TextToSpeech(data) -> None:
    rospy.loginfo("[Debug] tts called.")
    filename = data.data
    path = env.VOICE_PATH + "/" + filename + ".mp3"
    try:
        playsound(path)
    except Exception as e:
        rospy.loginfo(f"[Error] Exception occurred: {e}")
    time.sleep(GetDurationOfMP3(path) + 1)

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
