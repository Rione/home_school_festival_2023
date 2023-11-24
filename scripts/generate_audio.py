#!/usr/bin/env python3

# Run this program to generate voice data as mp3.
import subprocess
from online_audio_kit import AudioKit

prefix = (subprocess.run("find ~/catkin_ws/src/home_school_festival_2023 -name voice", shell=True, capture_output=True, text=True)).stdout + '/'

audio = AudioKit('ja')
audio.tts("何色の紙袋をお持ちしましょうか?", mode="gen", path=prefix + "ask_color.mp3")
audio.tts("わかりました。しろ色の紙袋をお持ちします。", mode="gen", path=prefix + "info_white.mp3")
audio.tts("わかりました。茶色の紙袋をお持ちします。", mode="gen", path=prefix + "info_brown.mp3")
audio.tts("しろ色の紙袋をのせてください。", mode="gen", path=prefix + "ask_white.mp3")
audio.tts("茶色の紙袋をのせてください。", mode="gen", path=prefix + "ask_brown.mp3")
audio.tts("紙袋をお取りください。", mode="gen", path=prefix + "ask_bag.mp3")
audio.tts("目標地点へ移動します。", mode="gen", path=prefix + "info_move_target.mp3")
audio.tts("目標地点へ到達しました。", mode="gen", path=prefix + "info_arrive_target.mp3")
audio.tts("ホームへ戻ります。", mode="gen", path=prefix + "info_move_origin.mp3")
audio.tts("すみません、聞き取れませんでした。もう一度言ってください。", mode="gen", path=prefix + "err_ask_color.mp3")
audio.tts("移動する方向を指さしてください。", mode="gen", path=prefix + "ask_direction.mp3")

