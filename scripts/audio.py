#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from online_audio_kit import AudioKit


def CreateAudioProcessingNode():
    # Configurable variables
    node_name = 'audio_processing'
    topic_name = 'audio_processing'
    rate: int = 5       # hz

    # Node publisher
    pub = rospy.Publisher(topic_name, String, queue_size=1)
    rospy.init_node(node_name, anonymous=True)
    rate = rospy.Rate(rate)

    # Main
    audio = AudioKit('ja') # Option : AudioKit(language= 'ja' | 'en', openai_api_key=str)
    audio.tts("こんにちは。何色の紙袋をお持ちしましょうか?")

    for text in audio.vosk():
        rospy.loginfo(text)
        if ('茶' in text):
            result = 'brown'
            break
        elif('白' in text):
            result = 'white'
            break
        
    audio.tts(f"わかりました。{'茶' if result == 'brown' else '白'}色の紙袋をお持ちします。")

    while not rospy.is_shutdown():
        rospy.loginfo(f"Bag color: {result}")
        pub.publish(result)
        rate.sleep()

if __name__ == '__main__':
    try:
        CreateAudioProcessingNode()
    except rospy.ROSInterruptException:
        pass

