#!/usr/bin/env python3

import rospy
import time
import env
from std_msgs.msg import String
from std_srvs.srv import SetBool, SetBoolResponse
from online_audio_kit import AudioKit


# Create an instance of AudioKit
vosk_model_name = env.MODEL_NAME if(env.MODEL_NAME != "") else None
AUDIO = AudioKit('ja', vosk_model_name=vosk_model_name)

def CheckIfTextInclude(text:str, words) -> bool:
    for word in words:
        bool = word in text
        if(bool):
            return True
    return False

def SpeechRecognition() -> str:
    color:str = None
    words_white = ["しろ","白"]
    words_brown = ["ちゃ","茶","サイロ"]
    words_yellow = ["きいろ","黄色"]
    words_red = ["あか","赤"]

    try:
        for text in AUDIO.vosk():
            if(CheckIfTextInclude(text, words_white)):
                color = 'white'
                break
            elif(CheckIfTextInclude(text, words_brown)):
                color = 'brown'
                break
            elif(CheckIfTextInclude(text, words_yellow)):
                color = 'yellow'
                break
            elif(CheckIfTextInclude(text, words_red)):
                color = 'red'
                break
            else: continue
        # if the for-loop ends up without break
        else: 
            pub_tts.publish("err_audio")
            rospy.wait_for_message("topic_tts_finished", String, timeout=None)
    except Exception as e:
        rospy.loginfo(f'[Error] Exception occurred: {e}')
    
    return color

def AskWhichColor() -> str:
    boolean: bool = False
    while not (boolean):
        pub_tts.publish("ask_color")
        rospy.wait_for_message("topic_tts_finished", String, timeout=None)

        result = SpeechRecognition()
        time.sleep(0.5)

        if(result == 'white'):
            pub_tts.publish("info_white")
        elif(result == 'brown'):
            pub_tts.publish("info_brown")
        elif(result == 'yellow'):
            pub_tts.publish("info_yellow")
        elif(result == 'red'):
            pub_tts.publish("info_red")
        rospy.wait_for_message("topic_tts_finished", String, timeout=None)

        pub_tts.publish("ask_yes_or_no")
        rospy.wait_for_message("topic_tts_finished", String, timeout=None)

        boolean = AskYesOrNo()
        
    rospy.loginfo(f"[Debug] Set color to: '{result}'")
    pub_tts.publish("info_acknowledged")
    rospy.wait_for_message("topic_tts_finished", String, timeout=None)

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
            rospy.wait_for_message("topic_tts_finished", String, timeout=None)
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

