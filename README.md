# home_school_festival_2023
branch for docker env, without arm pkg(12.05時点)


**以下、Dockerが導入されていることを前提とします。**
Dockerを使用しない場合は、productionブランチを利用してください。


### 0. docker-compose.yamlを書き換える
ローカル上で、マップデータが存在するディレクトリの**絶対パス**を予め取得します。<br>
`docker-compose.yaml`の以下の行の該当箇所を絶対パスに書き換え、コメントを外します。
```xml
volumes:
#   - {ここに絶対パス}:/root/map
```
完成例:
```xml
volumes:
    - /home/usr/map:/root/map
```
`$DISPLAY`やpulseサーバのディレクトリなど、各自の環境に応じて適宜変更してください。<br>
ただし、Linux環境であれば、多くの場合初期値のままでいけると思います。


### 1. Dockerイメージを作成する(初回のみ)
`Dockerfile`が存在するディレクトリに移動します。<br>
そこで、以下のコマンドを実行します。
```bash
docker build .
```
これでDockerイメージが作成できます。<br>
**10~20分程度**かかりますので、時間に余裕を持って実行してください。


### 2. Dockerコンテナを起動する
`docker-compose.yaml`が存在するディレクトリに移動します。<br>
以下のコマンドを実行します。
```bash
docker compose up -d
# すでに作成済みのコンテナがある場合は、
docker compose start -d
```
これでDockerコンテナが起動します。<br>
確認したい場合は、
```bash
docker container list
```
を実行してください。


### 3. catkin_wsの準備をする
以下のコマンドを実行してください。
```bash
cd /root/catkin_ws && \
catkin_make && \
source devel/setup.bash
```


### 4. env.pyを書き換える
`MODEL_NAME`で、使用したいVOSKモデルを指定できます。(任意)<br>
VOSKモデルを使用することで高精度の音声認識が可能になる一方、約1GBのディスク容量と最大16GBのメモリを必要とします。<br>
VOSKモデルの一覧は、こちらを参照:[VOSK Models](https://alphacephei.com/vosk/models)

また、目標地点への座標を指定します。`[X, Y, Z]`となるように数値を入力してください。


### 5. test.launchを書き換える
`test.launch`ファイル中の以下の記述を確認します。
```xml
<include file="$(find nav_lecture)/launch/navigation.launch" >
    <arg name="map_file" value="/root/map/{マップのファイル名}.yaml" >
</include>
```
`value=`の後に、使用するマップデータの**ファイル名**を指定してください。<br>
この際、パス(`/root/map/`)は変更しないように注意してください。


### 5. launchファイルを実行する
launchファイルの起動には、次のコマンドを実行してください。
```bash
roslaunch home_school_festival_2023 test.launch
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


### 6. Dockerコンテナを終了・破棄する
終了したい場合は、
```bash
docker compose stop
```
破棄したい場合は、
```bash
docker compose down
```
を実行してください。

破棄した場合、再度実行する際には`env.py`や`test.launch`を書き換える必要があります。<br>
また、Dockerコンテナは破棄されますがDockerイメージは破棄されません。