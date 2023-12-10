#!/usr/bin/env python3

from Controller import Controller


def main(ctrl):
    ctrl: Controller = Controller()

    # Wait for the current position to be given to Rviz
    print('[Info] Specify the current position of the turtlebot.')
    ctrl.WaitForSettingUp()

    # Wait for color and direction to be given
    print('[Info] Listening to topic_color and topic_direction.')
    ctrl.ListenToTopicColor()
    ctrl.ListenToTopicDirection()
    print('[Info] Moving to the target.')
    
    # Move to the 1st target
    ctrl.PublishTopicMove('target1' if(ctrl.direction == 'left') else 'target2') 
    print('[Info] topic_move published.')
    ctrl.ReceiveTheBag()

    # Move to the 2nd target
    ctrl.PublishTopicMove('target1' if(ctrl.direction == 'right') else 'target2')
    print('[Info] topic_move published.')
    ctrl.GiveTheBag()

    # Go back to the origin
    ctrl.PublishTopicMove('origin')
    print('[Info] topic_move published.')

    ctrl.ResetCostMaps()
    print('[Info] main_node has been terminated.')
    

if __name__ == '__main__':
    # Create an instance / node
    ctrl: Controller = Controller()
    try:
        main(ctrl)
    except Exception as e:
        ctrl.ResetCostMaps()
        print(f"[Error] Exception occurred: {e}")
