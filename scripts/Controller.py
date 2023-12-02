import rospy
import time
from std_msgs.msg import String
from std_srvs.srv import SetBool
from open_manipulator_x_pkg.srv import MoveArm


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

        # Publishers
        self.pub_mov = rospy.Publisher('topic_move', String, queue_size=1)
        self.pub_tts = rospy.Publisher('topic_tts', String, queue_size=1)

    def WaitForSettingUp(self):
        rospy.loginfo('[Info] Waiting for the server.')
        rospy.wait_for_service('srv_init_audio')

        self.pub_tts.publish("ask_config")
        time.sleep(4)

        try:
            while(True):
                service_call = rospy.ServiceProxy('srv_init_audio', SetBool)
                resp = service_call(False) # YesOrNo
                if(resp.success == True): break
        except rospy.ServiceException as e:
            rospy.loginfo("[Error] Service call failed: %s" % e)
        self.pub_tts.publish("info_acknowledged")
        time.sleep(5)

        rospy.loginfo("[Info] Promgram started.")
        self.pub_tts.publish("start")
        time.sleep(2)

        return

    def ListenToTopicDirection(self):
        rospy.wait_for_service('srv_init_camera')
        try:
            service_call = rospy.ServiceProxy('srv_init_camera', SetBool)
            resp = service_call(True) 
        except rospy.ServiceException as e:
            rospy.loginfo("[Error] Service call failed: %s" % e)
        self.direction = resp.message
        rospy.loginfo(f"[Debug] topic_direction received: {self.direction}") 

    def ListenToTopicColor(self):
        rospy.wait_for_service('srv_init_audio')
        try:
            service_call = rospy.ServiceProxy('srv_init_audio', SetBool)
            resp = service_call(True) # Color
        except rospy.ServiceException as e:
            rospy.loginfo("[Error] Service call failed: %s" % e)
        self.color = resp.message
        rospy.loginfo(f"[Debug] topic_color received: {self.color}")  

        return 

    def PublishTopicMove(self, target):
        """
        Publish topic_move; move to the target
        """
        if(target == 'origin'): 
            self.pub_tts.publish("info_origin")
        elif(target == 'target1'): 
            self.pub_tts.publish("info_target1")
        elif(target == 'target2'): 
            self.pub_tts.publish("info_target2")
        else:
            rospy.loginfo("[Error] Invalid target given.")
        time.sleep(2)

        self.pub_mov.publish(target)
        # Wait until the robot arrives at the target location
        rospy.wait_for_message('topic_nav_finished', String, timeout=None)
        rospy.loginfo("[Info] Navigation successfully finished.")

        if(target == 'origin'):
            self.pub_tts.publish("end")
            time.sleep(2)

        return

    def ReceiveTheBag(self):
        """
        Handle the arrival at the 1st target.
        """
        rospy.loginfo('[Info] Arrived at the 1st target.')
        
        self.pub_tts.publish("info_arrive_target")
        time.sleep(2)

        rospy.loginfo('[Info] Waiting for the server.')
        rospy.wait_for_service('srv_init_audio')

        # Arm
        rospy.wait_for_service('move_arm')
        try:
            control_arm = rospy.ServiceProxy('move_arm', MoveArm)

            if(self.color == 'white'):
                self.pub_tts.publish('ask_white')
            elif(self.color == 'brown'):
                self.pub_tts.publish('ask_brown')
            elif(self.color == 'yellow'):
                self.pub_tts.publish('ask_yellow')
            elif(self.color == 'red'):
                self.pub_tts.publish('ask_red')
            control_arm(0, 0, 0, 0)
            time.sleep(2)

            self.pub_tts.publish('check_place')
            control_arm(30, 20, 30, 2)
            time.sleep(3)

            while(True):
                service_call = rospy.ServiceProxy('srv_init_audio', SetBool)
                resp = service_call(False) # YesOrNo
                if(resp.success == True): break
            control_arm(0, 0, 0, 0)
            time.sleep(2)
        except rospy.ServiceException as e:
            rospy.loginfo("[Error] Service call failed: %s" % e)

        return

    def GiveTheBag(self):
        """
        Handle the arrival at the 2nd target.
        """
        rospy.loginfo('[Info] Arrived at the 2nd target.')
        self.pub_tts.publish("info_arrive_target")
        time.sleep(2)

        rospy.loginfo('[Info] Waiting for the server.')
        rospy.wait_for_service('srv_init_audio')

        # Arm
        rospy.wait_for_service('move_arm')
        try:
            control_arm = rospy.ServiceProxy('move_arm', MoveArm)

            self.pub_tts.publish("info_bag")
            control_arm(30, 20, 30, 2)
            time.sleep(2)
            
            self.pub_tts.publish("check_receive")
            time.sleep(2)

            while(True):
                service_call = rospy.ServiceProxy('srv_init_audio', SetBool)
                resp = service_call(False) # YesOrNo
                if(resp.success == True): break
            control_arm(0, 0, 0, 0)
            time.sleep(2)
        except rospy.ServiceException as e:
            rospy.loginfo("[Error] Service call failed: %s" % e)

        return


