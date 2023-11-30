#!/usr/bin/env python3

ENV_PATH = ""

import rospy
import time
import os
from dotenv import load_dotenv
from std_msgs.msg import String
from online_audio_kit import AudioKit


load_dotenv(dotenv_path=ENV_PATH)
# Create an instance of AudioKit
AUDIO = AudioKit('ja') # Option : AudioKit(language= 'ja' | 'en', openai_api_key=str)

def SpeechRecognition() -> str:
    color:str = None
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
                TextToSpeech("err_audio")
                time.sleep(3)
                continue
        except Exception as e:
            rospy.loginfo(f'[Error] Exception occurred: {e}')
    
    return color

def AskWhichColor() -> None:
    pub = rospy.Publisher('topic_color', String, queue_size=1)

    TextToSpeech("ask_color")

    boolean:str = None
    while(boolean != 'yes'):
        color = SpeechRecognition()
        if(color == 'white'):
            TextToSpeech("info_white")
        elif(color == 'brown'):
            TextToSpeech("info_brown")
        time.sleep(3)
        boolean = AskYesOrNo()
        
    rospy.loginfo(f"[Debug] Set color to: '{color}'")
    time.sleep(2)
    
    try:
        pub.publish(color) # Publish a topic without waiting for the subscriber being established
    except Exception as e: 
        rospy.loginfo(f"[Error] Exception occurred: {e}")

    return

def AskYesOrNo() -> bool:
    pub = rospy.Publisher('topic_end_yes', String, queue_size=10)

    TextToSpeech("ask_yes_or_no")

    boolean:str = None
    try:
        for text in AUDIO.vosk():
            if("はい" in text):
                boolean = 'yes'
                break
            elif("いいえ" in text):
                boolean = 'no'
                break
            else: continue
        # if the for-loop ends up without break
        else: 
            TextToSpeech("err_audio")
            time.sleep(3)
    except Exception as e:
        rospy.loginfo(f'[Error] Exception occurred: {e}')
    
    try:
        pub.publish(boolean) # Publish a topic without waiting for the subscriber being established
    except Exception as e: 
        rospy.loginfo(f"[Error] Exception occurred: {e}")

    return boolean

def TextToSpeech(obj) -> None:
    """
    Take an object as the parameter; object.data = "{name_of_the_audio_file}" 
    """
    rospy.loginfo("[Debug] tts called.")
    prefix = os.getenv('VOICE_PATH')
    try:
        AUDIO.play(prefix + obj + '.mp3')
    except Exception as e:
        rospy.loginfo(f"[Error] Exception occurred: {e}")

    return

def Router(data) -> None:
    signal = data.data
    if(signal == "start_mic"):
        AskWhichColor()
    elif(signal == "start_yes"):
        AskYesOrNo()
    else:
        TextToSpeech(data)

def main() -> None:
    rospy.init_node('audio_node', anonymous=True)
    rospy.Subscriber("topic_audio", String, Router)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()        
    except rospy.ROSInterruptException:
        pass

