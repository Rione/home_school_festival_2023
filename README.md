# home_school_festival_2023
(As of 24th Oct)

## やることリスト
- [ ] メインノード(main.py)
- [ ] 音声ノード(audio.py)
- [ ] 画像ノード(finger.py)

## 役立つサイト
- [[ROS] Turtlebot2でナビゲーションする](https://shutotamaoka.xyz/memo/ros-navigation-on-turtlebot2-ja/) (Shutoさんの記事)
- [Online Audio Kit](https://github.com/rionehome/online_audio_kit) (rionehomeのレポジトリ)
- [Writing a Simple Publisher and Subscriber (Python)](https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29) (ROS tutorial)
- [Using Git source control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview) (GitのGUI操作)
- [Semantic Commit Messages](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716) (commitメッセージの書き方例)

### 提案
- ~~ユニークな処理を音声・画像等のノードに含めると、それらの汎用性が低下してしまいます。ノードは、データ受け渡しの端点としてなるべく共通する処理のみを含め、以降の個別具体的な処理は、他のファイルにクラスなどを別途作成し、そのメソッドとして記述すると見通しが良いものと思われます。~~　→通信がかえって煩雑になるため、main.py以外のファイルは独立して処理を書く方が効率的だと結論しました。
