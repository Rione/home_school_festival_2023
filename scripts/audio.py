#!/usr/bin/env python3

import rospy
import time
import os
from dotenv import load_dotenv
from std_msgs.msg import String
from online_audio_kit import AudioKit


# Create an instance of AudioKit
AUDIO = AudioKit('ja') # Option : AudioKit(language= 'ja' | 'en', openai_api_key=str)

load_dotenv()

def CreateAudioProcessingNode():
    # Node and publisher
    rospy.init_node('audio_node', anonymous=True)
    pub = rospy.Publisher('topic_color', String, queue_size=10)

    TextToSpeech("ask_color")

    color = None
    while(color == None):
        try:
            for text in AUDIO.vosk():
                if("白" in text):
                    color = 'white'
                    break
                elif("茶" in text):
                    color = 'brown'
                    break
                else: continue
            # if the for-loop ends up without break
            else: 
                TextToSpeech("err_ask_color")
                time.sleep(3)
                continue
        except Exception as e:
            rospy.loginfo(f'[Error] Exception occurred: {e}')
        
    rospy.loginfo(f"[Debug] Set color to: '{color}'")
    time.sleep(2)

    if(color == 'white'):
        TextToSpeech("info_white")
    elif(color == 'brown'):
        TextToSpeech("info_brown")
    time.sleep(3)
    
    try:
        pub.publish(color) # Publish a topic without waiting for the subscriber being established
    except Exception as e: 
        rospy.loginfo(f"[Error] Exception occurred: {e}")

def TextToSpeech(obj):
    """
    Take an object as the parameter; object.data = "{name_of_the_audio_file}" 
    """
    rospy.loginfo("[Debug] tts called.")
    prefix = os.getenv('VOICE_PATH')
    try:
        AUDIO.play(prefix + obj + '.mp3')
    except Exception:
        AUDIO.play(prefix + obj.data + '.mp3')

def ListenToTopicTTS():
    rospy.Subscriber("topic_tts", String, TextToSpeech)
    rospy.spin()

if __name__ == '__main__':
    try:
        CreateAudioProcessingNode()
        rospy.loginfo("[Debug] passed.")
        ListenToTopicTTS()
    except rospy.ROSInterruptException:
        pass

