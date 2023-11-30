# home_school_festival_2023
(11.30時点)

### >>注意<<
`audio_new.py`および`generate_audio_new.py`を実行するためには、**speech_and_NLP**パッケージのインポートが必要です。<br>
詳しくは[speech_and_NLP](https://github.com/rionehome/speech_and_NLP/tree/main)レポジトリを参照してください。

### 0. 必要なライブラリをインストールする
このプロジェクトでは.envファイルで環境変数を管理しているため、以下のインストールが必要です。
```bash
pip intall python-dotenv
```

### 1. .envファイルのパスを指定する
以下の４ファイルで、.envファイルの**絶対パス**を指定する必要があります。
- `audio.py`
- `send_goal.py`
- `generate_audio.py`
- `generate_audio_new.py`

以下の例のように書き換えてください。
```python
ENV_PATH = "/hoge/fuga/..../home_school_festival_2023/.env"
```

### 2. voiceディレクトリを作成する
`home_school_festival_2023`内に、`voice`ディレクトリがあることを確認してください。<br>
`home_school_festival_2023`内であればどこでも動作します。なければ、`mkdir voice`で作成してください。

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

launchファイルは次のノードを起動します:
- main_node
- audio_node
- finger_node
- send_goal_node


