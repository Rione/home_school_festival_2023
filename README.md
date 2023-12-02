# home_school_festival_2023
(12.01時点)

### >>注意<<
`audio_new.py`および`generate_audio_new.py`を実行するためには、**speech_and_NLP**パッケージのインポートが必要です。<br>
詳しくは[speech_and_NLP](https://github.com/rionehome/speech_and_NLP/tree/main)レポジトリを参照してください。

### 0. 必要なライブラリをインストールする
レポジトリ直下に移動し、以下のコマンドを実行します。
```bash
pip install -r requirements.txt
```
### 1. env.pyを書き換える
`VOICE_PATH`には、`voice`ディレクトリの**絶対パス**を指定する必要があります。(最後のスラッシュ不要)<br>
また、目標地点への座標を指定します。`[X, Y, Z]`となるように数値を入力してください。

### 2. 音声ファイルを生成する
読み上げ機能に使われる音声ファイル(.mp3)を生成してください。<br>
以下のコマンドを実行して、必要な音声ファイルを生成できます。
```bash
cd ~/catkin_ws/src/home_school_festival_2023/scripts
./generate_audio.py
```
NLP版パッケージを利用する場合は(.wavファイルでの出力)、
```bash
cd ~/catkin_ws/src/home_school_festival_2023/scripts
./generate_audio_new.py
```
生成された音声ファイルは、`voice`ディレクトリに格納されます。

### 3. 読み込むmapデータを指定する
launchファイル中の以下の記述を確認します。
```xml
<include file="$(find nav_lecture)/launch/navigation.launch" >
    <arg name="map_file" value="{ここに絶対パスを指定。以下の例を参照}" >
    <!-- <arg name="map_file" value="~/catkin_ws/src/home_school_festival_2023/map/bushitu.yaml" > -->
</include>
```
`value=`の後に、使用するmapデータの**絶対パス**を指定してください。

### 4. launchファイルを実行する
launchファイルの起動には、次のコマンドを実行してください。
```bash
roslaunch home_school_festival_2023 test.launch
```
NLP版の音声認識を利用する場合は、
```bash
roslaunch home_school_festival_2023 new.launch
```
launchファイルは次のlaunchファイルをインクルードします:
- minimal.launch
- rplidar.launch
- navigation.launch

launchファイルは次のノードを起動します:
- main_node
- stt_node
- tts_node
- finger_node
- send_goal_node


