from online_audio_kit import AudioKit

audio = AudioKit(language= "ja")

for text in audio.vosk():
    print(text)
    if '茶色' in text:
      print('成功')