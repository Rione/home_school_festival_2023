#!/usr/bin/env python3

# Run this program to generate voice data as mp3.
import env
from online_audio_kit import AudioKit

PREFIX = env.VOICE_PATH + "/"
# Create an instance of AudioKit
vosk_model_name = env.MODEL_NAME if(env.MODEL_NAME != "") else None
vosk_model_path = env.MODEL_PATH if(env.MODEL_PATH != "") else None
audio = AudioKit('ja', vosk_model_name=vosk_model_name, vosk_model_path=vosk_model_path)

audio.tts("準備が完了しました。", mode="gen", path=PREFIX + "start.mp3")
audio.tts("ロボットの現在地を指定してください。準備が完了したら、はい、とお知らせください。", mode="gen", path=PREFIX + "ask_config.mp3")
audio.tts("赤、白、黄色、茶色、どの色の紙袋を配達しましょうか。", mode="gen", path=PREFIX + "ask_color.mp3")
audio.tts("しろ色の紙袋を配達します。", mode="gen", path=PREFIX + "info_white.mp3")
audio.tts("茶色の紙袋を配達します。", mode="gen", path=PREFIX + "info_brown.mp3")
audio.tts("黄色の紙袋を配達します。", mode="gen", path=PREFIX + "info_yellow.mp3")
audio.tts("赤色の紙袋を配達します。", mode="gen", path=PREFIX + "info_red.mp3")
audio.tts("しろ色の紙袋を渡してください。", mode="gen", path=PREFIX + "ask_white.mp3")
audio.tts("茶色の紙袋を渡してください。", mode="gen", path=PREFIX + "ask_brown.mp3")
audio.tts("黄色の紙袋を渡してください。", mode="gen", path=PREFIX + "ask_yellow.mp3")
audio.tts("赤色の紙袋を渡してください。", mode="gen", path=PREFIX + "ask_red.mp3")
audio.tts("紙袋をお取りください。", mode="gen", path=PREFIX + "info_bag.mp3")
audio.tts("ホームへ戻ります。", mode="gen", path=PREFIX + "info_origin.mp3")
audio.tts("わかりました。移動します。", mode="gen", path=PREFIX + "info_target1.mp3")
audio.tts("わかりました。移動します。", mode="gen", path=PREFIX + "info_target2.mp3")
audio.tts("よろしいですか。はい、または、いいえ、とお答えください。", mode="gen", path=PREFIX + "ask_yes_or_no.mp3")
audio.tts("渡したら、はい、とお知らせください。", mode="gen", path=PREFIX + "check_place.mp3")
audio.tts("受け取ったら、はい、とお知らせください。", mode="gen", path=PREFIX + "check_receive.mp3")
audio.tts("わかりました。", mode="gen", path=PREFIX + "info_acknowledged.mp3")
audio.tts("目標地点へ到達しました。", mode="gen", path=PREFIX + "info_arrive_target.mp3")
audio.tts("すみません、聞き取れませんでした。もう一度言ってください。", mode="gen", path=PREFIX + "err_audio.mp3")
audio.tts("左右どちらか移動したい方向を指差してください。", mode="gen", path=PREFIX + "ask_direction.mp3")
audio.tts("ナビゲーションを終了します。", mode="gen", path=PREFIX + "end.mp3")

