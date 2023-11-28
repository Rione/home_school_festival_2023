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

        # Variables
        self.color: str = None    # 紙袋の色
        self.direction: str = None   # 進行方向

        rospy.loginfo("[Info] Setting up...")
        time.sleep(3)

        # Publishers
        self.pub_mov = rospy.Publisher('topic_move', String, queue_size=1)
        self.pub_tts = rospy.Publisher('topic_tts', String, queue_size=1)
    
    def ListenToBothTopics(self):
        rospy.loginfo("[Debug] Waiting for topic_direction to be published.")
        self.direction = rospy.wait_for_message('topic_direction', String, timeout=None)
        # while(self.direction == None):
        #     time.sleep(1)
        rospy.loginfo(f"[Debug] topic_direction received: {self.direction}")

        rospy.loginfo("[Debug] Waiting for topic_color to be published.")
        self.color = rospy.wait_for_message('topic_color', String, timeout=None)
        rospy.loginfo(f"[Debug] topic_color received: {self.color}")        

    def PublishTopicMove(self, target):
        """
        Publish topic_move; move to the target
        """
        if(target == 0): 
            data = 'origin'
            self.pub_tts.publish("info_move_origin")
        elif(target == 1): 
            data = 'target1'
            self.pub_tts.publish("info_move_target")
        elif(target == 2): 
            data = 'target2'
            self.pub_tts.publish("info_move_target")
        else: rospy.loginfo('[Error] Wrong parameter given.')

        time.sleep(3)
        self.pub_mov.publish(data)

        # Wait until the robot arrives at the target location
        rospy.loginfo('[Debug] result: ' + str(rospy.wait_for_message('topic_end_nav', String, timeout=None).data))

    def ReceiveTheBag(self):
        """
        Handle the arrival at the 1st target.
        """
        rospy.loginfo('[Info] Arrived at the 1st target.')
        rospy.loginfo('[Info] Start navigation to the next target soon.')
        self.pub_tts.publish("info_arrive_target")
        time.sleep(3)
        if (self.color == 'white'):
            self.pub_tts.publish('ask_white')
        elif(self.color == 'brown'):
            self.pub_tts.publish('ask_brown')
        time.sleep(3)

    def GiveTheBag(self):
        """
        Handle the arrival at the 2nd target.
        """
        rospy.loginfo('[Info] Arrived at the 2nd target.')
        rospy.loginfo('[Info] Start navigation to the next target soon.')
        self.pub_tts.publish("ask_bag")
        time.sleep(3)


