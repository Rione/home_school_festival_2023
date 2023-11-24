# home_school_festival_2023
(As of 20th Nov.)

### 1. Generate audio files
Before running .launch file, you need to generate audio files by executing commands below. <br>
This will create mp3 files under voice directory.
```bash
cd ~/catkin_ws/src/home_school_festival_2023/scripts
./generate_audio.py
```

### 2. Run .launch file
This will launch 4 nodes with each separate terminal:
- main_node
- audio_node
- finger_node
- send_goal_node
```bash
roslaunch home_school_festival_2023 test.launch
```

