#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import String
from online_audio_kit import AudioKit

# Configurable variables
node_name = 'audio_node'
topic_name = 'topic_color'

def CreateAudioProcessingNode():
    # Node publisher
    pub = rospy.Publisher(topic_name, String, queue_size=1)
    rospy.init_node(node_name, anonymous=True)

    # Create an instance of AudioKit
    audio = AudioKit('ja') # Option : AudioKit(language= 'ja' | 'en', openai_api_key=str)
    audio.tts("こんにちは。何色の紙袋をお持ちしましょうか?")
    
    for i, text in enumerate(audio.vosk()):
        if("白" in text):
            color = 'white'
        elif("茶" in text):
            color = 'brown'
        else: 
            if(i % 20 == 0):
                audio.tts("すみません、聞き取れませんでした。もう一度言ってください。")
            continue
        break

    time.sleep(2)
    audio.tts(f"わかりました。{'茶' if color == 'brown' else '白'}色の紙袋をお持ちします。")

    rospy.loginfo(f"[Debug] Set bagColor to '{color}'")
    pub.publish(color) # Publish a topic regardless of the subscriber already established or not

if __name__ == '__main__':
    try:
        CreateAudioProcessingNode()
    except rospy.ROSInterruptException:
        pass

