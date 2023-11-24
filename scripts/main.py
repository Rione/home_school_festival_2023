#!/usr/bin/env python3

from Controller import Controller


def main():
    # Create an instance / node
    ctrl: Controller = Controller()

    # Wait for color and direction being given
    print('[Info] Listening to topic_color and topic_direction.')
    ctrl.ListenToBothTopics()
    print('[Info] Moving to the target.')
    
    # Move to the first target
    ctrl.PublishTopicMove(1 if(ctrl.direction == 'left') else 2) # Left to 1, right to 2
    print('[Info] topic_move published.')
    ctrl.ReceiveTheBag()

    # Move to the second target
    ctrl.PublishTopicMove(2 if(ctrl.direction == 'left') else 1) # Move to the other side
    print('[Info] topic_move published.')
    ctrl.GiveTheBag()

    # Go back to the origin
    ctrl.PublishTopicMove(0)
    print('[Info] topic_move published.')

    print('[Info] main_node has been terminated.')
    

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"[Error] Exception occurred: {e}")