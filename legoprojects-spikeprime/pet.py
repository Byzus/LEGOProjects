from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
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
    hub.light_matrix.show_image: 'HAPPY'
    RLleg.run_to_position(270)
    RRleg.run_to_postion(90)
    hub.light_status.on('lime')
    tail_animation()


def sit():
    hub.light_matrix.show_image: 'HAPPY'
    legs.run_to_position(0)
    hub.status_light.on('green')
    tail.stop()


def sleep():
    tail.stop()
    hub.status_light.on('blue')
    hub.light_matrix.show_image: 'ASLEEP'


def pee():
    legs.stop()
    hub.light_status.on('yellow')
    RLleg.go_to_postition(270)
    RRleg.go_to_posiion(0)
    idle()


if hub.left_button.is_pressed():
    sit()

if hub.right_button.is_pressed():
    sleep()

gesture = hub.motion_sensor.wait_for_new_gesture()
if gesture == 'shaken':
    idle()
