#!/usr/bin/env python3

ENV_PATH = ""

import rospy
import time
from dotenv import load_dotenv
from std_msgs.msg import String
from std_srvs.srv import SetBool, SetBoolResponse
from online_audio_kit import AudioKit


# pub_color = rospy.Publisher('topic_color', String, queue_size=1)
# pub_bool = rospy.Publisher('topic_end_yes', String, queue_size=1)

load_dotenv(dotenv_path=ENV_PATH)
# Create an instance of AudioKit
AUDIO = AudioKit('ja') # Option : AudioKit(language= 'ja' | 'en', openai_api_key=str)

def SpeechRecognition() -> str:
    color:str = None
    words_white = set(["しろ","白"])
    words_brown = set(["ちゃ","茶","サイロ"])

    try:
        for text in AUDIO.vosk():
            text = set(text)
            if(not words_white.isdisjoint(text)):
                color = 'white'
                break
            elif(not words_brown.isdisjoint(text)):
                color = 'brown'
                break
            else: continue
        # if the for-loop ends up without break
        else: 
            pub_tts.publish("err_audio")
            time.sleep(3)
    except Exception as e:
        rospy.loginfo(f'[Error] Exception occurred: {e}')
    
    return color

def AskWhichColor() -> None:
    resp = SetBoolResponse()

    boolean: bool = False
    while not (boolean):
        pub_tts.publish("ask_color")
        time.sleep(2)

        color = SpeechRecognition()
        resp.message = color
        time.sleep(2)

        if(color == 'white'):
            pub_tts.publish("info_white")
        elif(color == 'brown'):
            pub_tts.publish("info_brown")
        time.sleep(2)

        pub_tts.publish("ask_yes_or_no")
        time.sleep(0.5)

        boolean = AskYesOrNo(internal=True)
        
    resp.success = True
    rospy.loginfo(f"[Debug] Set color to: '{color}'")
    pub_tts.publish("info_acknowledged")
    time.sleep(1)

    return resp

def AskYesOrNo(_, internal:bool=False) -> bool:
    resp = SetBoolResponse()

    try:
        for text in AUDIO.vosk():
            if("はい" in text):
                resp.success = True
                break
            elif("いいえ" in text):
                resp.success = False
                break
            else: continue
        # if the for-loop ends up without break
        else: 
            pub_tts.publish("err_audio")
            time.sleep(3)
    except Exception as e:
        rospy.loginfo(f'[Error] Exception occurred: {e}')

    resp.message= "True or False"
    if(internal): return resp.success
    else: return resp

if __name__ == '__main__':
    try:
        rospy.init_node('audio_node', anonymous=True)
        pub_tts = rospy.Publisher('topic_tts', String, queue_size=1)
        srv1 = rospy.Service('srv_init_audio', SetBool, AskWhichColor)
        srv2 = rospy.Service("srv_yes_or_no", SetBool, AskYesOrNo)
        print("stt_node: ready")
        rospy.spin() 
    except rospy.ROSInterruptException:
        pass

