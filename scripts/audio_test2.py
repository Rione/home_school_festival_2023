#!/usr/bin/env python3
from online_audio_kit import AudioKit
#from std_msgs.msg import String
audio = AudioKit(language = 'ja')

class AudioKit():
  shiro = '白'
  cha   = '茶色'
  for text in audio.vosk():
    if shiro in text:
      print('しろです')
      break
    elif cha in text:
      print('ちゃいろです')
      break

audio = AudioKit()

#if __name__ == "__main__":