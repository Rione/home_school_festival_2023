# home_school_festival_2023
(12.03時点)

### >>注意<<
`audio_new.py`および`generate_audio_new.py`を実行するためには、**speech_and_NLP**パッケージのインポートが必要です。<br>
詳しくは[speech_and_NLP](https://github.com/rionehome/speech_and_NLP/tree/main)レポジトリを参照してください。

### 0. 必要なパッケージをcloneする
ロボットアームを使用するために、以下のパッケージのcloneが必要です。
```bash
cd ~/catkin_ws/src/
git clone https://github.com/Rione/home_open_manipulator_x_pkg.git
sh setup.sh
cd ~/catkin_ws && catkin_make
```
始めて実行する場合には、udevルールを作成します:
```bash
rosrun open_manipulator_controller create_udev_rules
```

### 1. 必要なライブラリをインストール&アップデートする
`home_school_festival_2023`レポジトリ直下に移動し、以下のコマンドを実行します。
```bash
pip3 install -r requirements.txt
```
`online_audio_kit`をアップデートします。
```bash
pip3 install -U git+https://github.com/rionehome/online_audio_kit
```

### 2. env.pyを書き換える
`VOICE_PATH`には、`voice`ディレクトリの**絶対パス**を指定する必要があります。(最後のスラッシュ不要)<br>

`MODEL_PATH`あるいは`MODEL_NAME`では、使用したいVOSKモデルを指定できます。(任意)<br>
VOSKモデルを使用することで高精度の音声認識が可能になる一方、約1GBのディスク容量と最大16GBのメモリを必要とします。<br>
VOSKモデルの一覧は、こちらを参照:[VOSK Models](https://alphacephei.com/vosk/models)

また、目標地点への座標を指定します。`[X, Y, Z]`となるように数値を入力してください。

### 3. 音声ファイルを生成する
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

### 4. 読み込むmapデータを指定する
launchファイル中の以下の記述を確認します。
```xml
<include file="$(find nav_lecture)/launch/navigation.launch" >
    <arg name="map_file" value="{ここに絶対パスを指定。以下の例を参照}" >
    <!-- <arg name="map_file" value="~/catkin_ws/src/home_school_festival_2023/map/bushitu.yaml" > -->
</include>
```
`value=`の後に、使用するmapデータの**絶対パス**を指定してください。

### 5. launchファイルを実行する
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
- open_manipulator_controller.launch

launchファイルは次のノードを起動します:
- main_node
- stt_node
- tts_node
- finger_node
- send_goal_node


=======
(As of 16th Nov)

詳細は[Notion](https://www.notion.so/deabc891869b414280da43e14973c001?pvs=4)を参照。
