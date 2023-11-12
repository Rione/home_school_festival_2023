import rospy
from std_msgs.msg import String

class Controller():
    """
    A class for managing robot's movement and the connections between the nodes. 
    """
    def __init__(self):
        self.bagColor: str = None    # 紙袋の色
        self.direction: str = None   # 進行方向
    
    def ListenToBagColor(self):
        """
        Override current bag color.
        """
        self.bagColor = rospy.wait_for_message('topic_color', String, timeout=None)

    def ListenToDirection(self):
        """
        Override current direction.
        """
        self.direction = rospy.wait_for_message('topic_direction', String, timeout=None)