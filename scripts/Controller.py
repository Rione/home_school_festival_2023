import rospy
import time
from std_msgs.msg import String

class Controller():
    """
    A class for managing robot's movement and the connections between the nodes. 
    """
    def __init__(self):
        # Create a node
        rospy.init_node('main_node', anonymous=True)
        self.color: str = None    # 紙袋の色
        self.direction: str = None   # 進行方向
    
    def ListenToTopicColor(self):
        """
        Wait for topic_color published
        """
        self.color = rospy.wait_for_message('topic_color', String, timeout=None)

    def ListenToTopicDirection(self):
        """
        Wait for topic_direction published
        """
        self.direction = rospy.wait_for_message('topic_direction', String, timeout=None)

    def PublishTopicMove(self, target):
        """
        Publish topic_move; move to the target
        """
        pub_move = rospy.Publisher('topic_move', String, queue_size=1)
        pub_tts = rospy.Publisher('topic_tts', String, queue_size=1)
        if(target == 0): 
            result = 'origin'
            pub_tts.publish("ホームに戻ります")
            time.sleep(3)
        elif(target == 1): result = 'target1'
        elif(target == 2): result = 'target2'
        else: rospy.logdebug('[Debug] Wrong argument given.')

        pub_move.publish(result)

        rospy.logdebug('[Debug] result: ' + rospy.wait_for_message('topic_end_nav', String, timeout=None))

    def ReceiveTheBag(self):
        """
        Handle the arrival at the 1st target.
        """
        ## WIP
        pub_tts = rospy.Publisher('topic_tts', String, queue_size=1)
        pub_tts.publish("第一目標に到達しました。")
        rospy.logdebug('[Debug] Arrived at the 1st designated target.')
        rospy.logdebug('[Debug] Start navigation to the next target soon.')

    def GiveTheBag(self):
        """
        Handle the arrival at the 2nd target.
        """
        ## WIP
        pub_tts = rospy.Publisher('topic_tts', String, queue_size=1)
        pub_tts.publish("第二目標に到達しました。")
        rospy.logdebug('[Debug] Arrived at the 2nd designated target.')
        rospy.logdebug('[Debug] Start navigation to the next target soon.')

