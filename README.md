# home_school_festival_2023
(11.24時点)

### 1. voiceディレクトリを作成する
`home_school_festival_2023`内に、`voice`ディレクトリがあることを確認してください。<br>
直下にある必要はありません。なければ、`mkdir voice`で作成してください。

### 2. 音声ファイルを生成する
読み上げ機能に使われる音声ファイル(mp3)を生成してください。<br>
以下のコマンドを実行して、必要な音声ファイルを生成できます。
```bash
cd ~/catkin_ws/src/home_school_festival_2023/scripts
./generate_audio.py
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
launchファイルは次のlaunchファイルをincludeします:
- minimal.launch
- rplidar.launch
- navigation.launch

launchファイルは次のノードを起動します:
- main_node
- audio_node
- finger_node
- send_goal_node


