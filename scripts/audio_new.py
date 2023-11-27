#!/usr/bin/env python3

import rospy
import time
import subprocess
from std_msgs.msg import String
from speech_and_NLP.src.speechToText import recognize_speech
from speech_and_NLP.src.tools.speech_to_text.replaceFromDict import replaces
from speech_and_NLP.src.tools.speech_to_text.isMeaning import is_meaning
from speech_and_NLP.src.tools.text_to_speech.playAudio import playAudio

# Const variables
PRE:str = (subprocess.run("find ~/catkin_ws/src/home_school_festival_2023 -name voice", shell=True, capture_output=True, text=True)).stdout + '/'
DICT:str = (subprocess.run("find ~/catkin_ws/src/home_school_festival_2023 -name dict.json", shell=True, capture_output=True, text=True)).stdout

def CreateAudioProcessingNode():
    # Node and publisher
    rospy.init_node('audio_node', anonymous=True)
    pub = rospy.Publisher('topic_color', String, queue_size=1)

    TextToSpeech('ask_color')

    color = None
    while(color == None):
        try:
            text = recognize_speech(print_partial=True, use_break=10, remove_space=True, lang='ja')
            text = replaces(text=text, trdict=DICT)
            if(is_meaning(text=text, word_list=['白', 'しろ', 'シロ'], path='')):
                color = 'white'
                break
            elif(is_meaning(text=text, word_list=['茶', 'ちゃ', 'チャ'], path='')):
                color = 'brown'
                break 
            else:
                TextToSpeech('err_ask_color')
                time.sleep(2)
                continue
        except Exception as e:
            rospy.loginfo(f'[Error] Exception occurred: {e}')
        
    rospy.loginfo(f"[Debug] Set color to: '{color}'")
    TextToSpeech(f"{'info_white' if color == 'white' else 'info_brown'}")
    time.sleep(3)
    
    if(color != None):
        pub.publish(color) # Publish a topic without waiting for the subscriber being established
    else: rospy.loginfo("[Error] The color is not given. Please try again.")

def TextToSpeech(obj):
    """
    Take an object as the parameter; object.data = "{name_of_the_audio_file}" 
    """
    try:
        playAudio(PRE + obj + '.wav')
    except TypeError:
        playAudio(PRE + obj.data + '.wav')

def main():
    CreateAudioProcessingNode()
    rospy.Subscriber("topic_tts", String, TextToSpeech)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass