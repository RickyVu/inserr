import pygame
import roslibpy
import time
import json


pygame.init()
pygame.joystick.init()

RATE = 1/60

if pygame.joystick.get_count() == 0:
    print("No joystick found.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

# ROSbridge connection
ros = roslibpy.Ros(host='localhost', port=9090)
ros.run()
print("Connection with ros bridge successful")

pub = roslibpy.Topic(ros, '/inserr/input/joystick_raw', 'std_msgs/String')

# original:
# left: (-1, 0), right: (1, 0), up: (0, 1), down: (0, -1)
# remap:
# [up, left, right, down] where up: 0|1, left: 0|1, right: 0|1, down: 0|1
def hat_remap(hat):
    return [hat[1] == 1, 
            hat[0] == -1, 
            hat[0] == 1, 
            hat[1] == -1]

# original:
# 0: A, 1: B, 2: X, 3: Y
# remap:
# 0: Y, 1: X, 2: B, 3: A
def rctr_remap(buttons : list) -> None:
    buttons[0], buttons[3] = buttons[3], buttons[0]
    buttons[1], buttons[2] = buttons[2], buttons[1]



try:
    while True:
        pygame.event.pump()
        
        # Read joystick axes
        axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
        
        # Read joystick buttons
        buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]

        #dpad_up = hat[1] == 1
        #dpad_left = hat[0] == -1
        #dpad_right = hat[0] == 1
        #dpad_down = hat[1] == -1
        rctr_remap(buttons)

        

        message = {
            'axes': axes,
            'buttons': buttons,
            'hat': hat_remap(joystick.get_hat(0))
        }
        
        json_message = json.dumps(message)
        
        pub.publish(roslibpy.Message({'data': json_message}))
        
        time.sleep(RATE)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    pub.unadvertise()
    ros.terminate()
    pygame.quit()