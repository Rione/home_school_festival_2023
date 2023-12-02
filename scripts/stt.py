#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import String
from std_srvs.srv import SetBool, SetBoolResponse
from online_audio_kit import AudioKit


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

def AskWhichColor() -> str:
    boolean: bool = False
    while not (boolean):
        pub_tts.publish("ask_color")
        time.sleep(2)

        result = SpeechRecognition()
        time.sleep(2)

        if(result == 'white'):
            pub_tts.publish("info_white")
        elif(result == 'brown'):
            pub_tts.publish("info_brown")
        time.sleep(2)

        pub_tts.publish("ask_yes_or_no")
        time.sleep(0.5)

        boolean = AskYesOrNo()
        
    rospy.loginfo(f"[Debug] Set color to: '{result}'")
    pub_tts.publish("info_acknowledged")
    time.sleep(1)

    return result

def AskYesOrNo() -> bool:
    result = None
    try:
        for text in AUDIO.vosk():
            if("はい" in text):
                result = True
                break
            elif("いいえ" in text):
                result = False
                break
            else: continue
        # if the for-loop ends up without break
        else: 
            pub_tts.publish("err_audio")
            time.sleep(3)
    except Exception as e:
        rospy.loginfo(f'[Error] Exception occurred: {e}')

    return result

def Router(data):
    resp = SetBoolResponse()
    if(data.data):
        resp.message = AskWhichColor()
        resp.success = True
    else:
        resp.success = AskYesOrNo()
        resp.message = "yes or no"

    return resp

if __name__ == '__main__':
    try:
        rospy.init_node('audio_node', anonymous=True)
        pub_tts = rospy.Publisher('topic_tts', String, queue_size=1)
        srv = rospy.Service('srv_init_audio', SetBool, Router)
        print("stt_node: ready")
        rospy.spin() 
    except rospy.ROSInterruptException:
        pass

