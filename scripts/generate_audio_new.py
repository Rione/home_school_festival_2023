#!/usr/bin/env python3

ENV_PATH = ""

import os
from dotenv import load_dotenv
from speech_and_NLP.src.tools.text_to_speech.textToWav import textToWav


load_dotenv(dotenv_path=ENV_PATH)
PREFIX = os.getenv('VOICE_PATH')

if __name__ == '__main__':
    try:
        textToWav(speed=1.0, path=PREFIX+'ask_color.wav', text='何色の紙袋をお持ちしましょうか?')
        textToWav(speed=1.0, path=PREFIX+'ask_direction.wav', text='移動する方向を指さしてください。')
        textToWav(speed=1.0, path=PREFIX+'ask_white.wav', text='しろ色の紙袋をのせてください。')
        textToWav(speed=1.0, path=PREFIX+'ask_brown.wav', text='茶色の紙袋をのせてください。')
        textToWav(speed=1.0, path=PREFIX+'ask_bag.wav', text='紙袋をお取りください。')
        textToWav(speed=1.0, path=PREFIX+'info_white.wav', text='わかりました。しろ色の紙袋をお持ちします。')
        textToWav(speed=1.0, path=PREFIX+'info_brown.wav', text='わかりました。茶色の紙袋をお持ちします。')
        textToWav(speed=1.0, path=PREFIX+'info_move_target.wav', text='目標地点へ移動します。')
        textToWav(speed=1.0, path=PREFIX+'info_arrive_target.wav', text='目標地点へ到達しました。')
        textToWav(speed=1.0, path=PREFIX+'info_move_origin.wav', text='ホームへ戻ります。')
        textToWav(speed=1.0, path=PREFIX+'err_ask_color.wav', text='すみません、聞き取れませんでした。もう一度言ってください。')
    except Exception as e:
        print(f"[Debug] Exception occured: {e}")
