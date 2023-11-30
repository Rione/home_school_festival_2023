#!/usr/bin/env python3

ENV_PATH = ""

# Run this program to generate voice data as mp3.
import os
from dotenv import load_dotenv
from online_audio_kit import AudioKit

load_dotenv(dotenv_path=ENV_PATH)
PREFIX = os.getenv('VOICE_PATH')

audio = AudioKit('ja')
audio.tts("何色の紙袋をお持ちしましょうか?", mode="gen", path=PREFIX + "ask_color.mp3")
audio.tts("わかりました。しろ色の紙袋をお持ちします。", mode="gen", path=PREFIX + "info_white.mp3")
audio.tts("わかりました。茶色の紙袋をお持ちします。", mode="gen", path=PREFIX + "info_brown.mp3")
audio.tts("しろ色の紙袋をのせてください。", mode="gen", path=PREFIX + "ask_white.mp3")
audio.tts("茶色の紙袋をのせてください。", mode="gen", path=PREFIX + "ask_brown.mp3")
audio.tts("紙袋をお取りください。", mode="gen", path=PREFIX + "ask_bag.mp3")
audio.tts("よろしければ、はい、訂正したければ、いいえ、とお答えください。", mode="gen", path=PREFIX + "ask_yes_or_no.mp3")
audio.tts("目標地点へ移動します。", mode="gen", path=PREFIX + "info_move_target.mp3")
audio.tts("目標地点へ到達しました。", mode="gen", path=PREFIX + "info_arrive_target.mp3")
audio.tts("ホームへ戻ります。", mode="gen", path=PREFIX + "info_move_origin.mp3")
audio.tts("すみません、聞き取れませんでした。もう一度言ってください。", mode="gen", path=PREFIX + "err_audio.mp3")
audio.tts("移動する方向を指さしてください。", mode="gen", path=PREFIX + "ask_direction.mp3")

