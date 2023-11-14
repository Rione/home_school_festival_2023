#!/usr/bin/env python3
import time
from Controller import Controller

def main():
    # Create an instance / node
    ctrl: Controller = Controller()

    ctrl.ListenToTopicColor()
    ctrl.ListenToTopicDirection()
    print('[Debug] Listening to topic_color and topic_direction.')

    debug_counter = 0
    # Wait for both color and direction to be specified
    while(ctrl.bagColor == None or ctrl.direction == None):
        print(f'[Debug] Waiting for color and direction. Time elapsed: {debug_counter}s')
        time.sleep(1)
        debug_counter = debug_counter + 1
    
    ctrl.PublishTopicMove(1 if(ctrl.direction == 'left') else 2) # Left to 1, right to 2
    ctrl.ReceiveTheBag()
    time.sleep(3)

    ctrl.PublishTopicMove(2 if(ctrl.direction == 'left') else 1) # Move to the other side
    ctrl.GiveTheBag()
    time.sleep(3)

    ctrl.PublishTopicMove(0) # Return to the Origin

    print('[Debug] Programme terminated.')
    

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An exception has been occurred during the execution: {e}")