#!/usr/bin/env python3

# Run this program to generate voice data as mp3.
import env
from online_audio_kit import AudioKit

PREFIX = env.VOICE_PATH

audio = AudioKit('ja')
audio.tts("しろ色と茶色、どちらの紙袋をお持ちしましょうか。", mode="gen", path=PREFIX + "ask_color.mp3")
audio.tts("しろ色の紙袋をお持ちします。", mode="gen", path=PREFIX + "info_white.mp3")
audio.tts("茶色の紙袋をお持ちします。", mode="gen", path=PREFIX + "info_brown.mp3")
audio.tts("しろ色の紙袋をのせてください。", mode="gen", path=PREFIX + "ask_white.mp3")
audio.tts("茶色の紙袋をのせてください。", mode="gen", path=PREFIX + "ask_brown.mp3")
audio.tts("紙袋をお取りください。", mode="gen", path=PREFIX + "info_bag.mp3")
audio.tts("1番目標へ移動します。", mode="gen", path=PREFIX + "info_target1.mp3")
audio.tts("2番目標へ移動します。", mode="gen", path=PREFIX + "info_target2.mp3")
audio.tts("よろしいですか。", mode="gen", path=PREFIX + "ask_yes_or_no.mp3")
audio.tts("紙袋を置いたら、はい、とお知らせください。", mode="gen", path=PREFIX + "check_place.mp3")
audio.tts("受け取ったら、はい、とお知らせください。", mode="gen", path=PREFIX + "check_recieve.mp3")
audio.tts("わかりました。", mode="gen", path=PREFIX + "info_acknowledged.mp3")
audio.tts("目標地点へ移動します。", mode="gen", path=PREFIX + "info_move_target.mp3")
audio.tts("目標地点へ到達しました。", mode="gen", path=PREFIX + "info_arrive_target.mp3")
audio.tts("ホームへ戻ります。", mode="gen", path=PREFIX + "info_move_origin.mp3")
audio.tts("すみません、聞き取れませんでした。もう一度言ってください。", mode="gen", path=PREFIX + "err_audio.mp3")
audio.tts("左右どちらか移動したい方向を指差してください。", mode="gen", path=PREFIX + "ask_direction.mp3")

