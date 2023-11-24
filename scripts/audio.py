#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import String
from online_audio_kit import AudioKit


def CreateAudioProcessingNode(audio):
    # Node and publisher
    rospy.init_node('audio_node', anonymous=True)
    pub = rospy.Publisher('topic_color', String, queue_size=1)

    TextToSpeech({'data': 'ask_color'}, audio)

    color = None
    while(color == None):
        try:
            for text in audio.vosk():
                if("白" in text):
                    color = 'white'
                    break
                elif("茶" in text):
                    color = 'brown'
                    break
                else: continue
            # if the for-loop ends up without break
            else: 
                TextToSpeech({'data': 'err_ask_color'}, audio)
                time.sleep(3)
                continue
        except Exception as e:
            rospy.loginfo(f'[Error] Exception occurred: {e}')
        
    rospy.loginfo(f"[Debug] Set color to: '{color}'")
    TextToSpeech({'data': f"{'info_white' if color == 'white' else 'info_brown'}"}, audio)
    time.sleep(3)
    
    if(color != None):
        pub.publish(color) # Publish a topic without waiting for the subscriber being established
    else: rospy.loginfo("[Error] The color is not given. Please try again.")

def TextToSpeech(obj, audio):
    """
    Take an object as the parameter; object.data = "{name_of_the_audio_file}" 
    """
    prefix = "../voice/" # Configure here to change directory to load audio from
    try:
        audio.play(prefix + obj["data"] + '.mp3')
    except TypeError:
        audio.play(prefix + obj.data + '.mp3')

if __name__ == '__main__':
    try:
        # Create an instance of AudioKit
        audio = AudioKit('ja') # Option : AudioKit(language= 'ja' | 'en', openai_api_key=str)

        CreateAudioProcessingNode()
        rospy.Subscriber("topic_tts", String, TextToSpeech)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

