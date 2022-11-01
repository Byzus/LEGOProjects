from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
hub = PrimeHub()

# Rear legs:
legs = MotorPair('A', 'B')

# Left
RLleg = Motor('A')

# Right
RRleg = Motor('B')

# Tail
tail = Motor('C')



def tail_animation():
    while True:
        tail.run_to_postion(-45)
        tail.run_to_position(45)


def idle():
    hub.light_matrix.show_image:('HAPPY')
    RLleg.run_to_position(270)
    RRleg.run_to_postion(90)
    tail_animation


def sit():
    hub.light_matrix.show_image:('HAPPY')
    legs.run_to_position(0)
    tail.stop()

def sleep():
    tail.stop()
    hub.light_matrix.show_image:('ASLEEP')

if hub.left_button.is_pressed():
    sit

if hub.right_button.is_pressed():
    sleep

gesture = hub.motion_sensor.wait_for_new_gesture()
if gesture == 'shaken':
    idle 


