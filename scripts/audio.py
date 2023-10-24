#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from online_audio_kit import AudioKit
from GptApi import GptApi

def CreateAudioProcessingNode():
    # Configurable variables
    node_name = 'audio_processing'
    topic_name = 'audio_processing'

    # Node publisher
    pub = rospy.Publisher(topic_name, String, queue_size=1)
    rospy.init_node(node_name, anonymous=True)

    # Create an instance of AudioKit
    audio = AudioKit('ja') # Option : AudioKit(language= 'ja' | 'en', openai_api_key=str)
    audio.tts("こんにちは。何色の紙袋をお持ちしましょうか?")

    counter = 0
    while True:
        recognized_text = audio.stt()
        color = GptApi.ExtractColor(recognized_text)
        if(color != 'brown' and color != 'white'):
            audio.tts("すみません、聞き取れませんでした。もう一度言ってください。")
            counter += 1
            if(counter > 5): 
                audio.tts("不具合が発生しました。プロセスを終了します。")
                exit()
        else: break  

    audio.tts(f"わかりました。{'茶' if color == 'brown' else '白'}色の紙袋をお持ちします。")

    rospy.loginfo(f"Set bagColor to '{color}'")
    pub.publish(color) # Publish a topic regardless of the subscriber already established or not

if __name__ == '__main__':
    try:
        CreateAudioProcessingNode()
    except rospy.ROSInterruptException:
        pass

