import rospy
from std_msgs.msg import String

class Controller():
    """
    A class for managing robot's movement and the connections between the nodes. 
    """
    def __init__(self) -> None:
        self.bagColor: str = None    # 紙袋の色
        self.direction: str = None   # 進行方向
    
    def SetBagColor(self) -> None:
        if(self.bagColor): return
        else:
            self.bagColor = rospy.wait_for_message('audio_processing', String, timeout=None)

    def SetDirection(self) -> None:
        if(self.direction): return
        else:
            self.direction = rospy.wait_for_message('finger_direction', String, timeout=None)