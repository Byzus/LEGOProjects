from ctypes import set_errno
from os import setegid
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()


hub.left_button.wait_until_pressed()

motorPair = MotorPair('A', 'F')
front_motor = Motor('A')
back_motor = Motor('F')
steering_motor = Motor('E')
hub.speaker.beep()

hub.light.matrix.off()


def forward_animation():
    # First number = x (from left)
    # Second number = y (from up
    # Example: hub.light_matrix.set_pixel(1, 4)

    hub.light_matrix.set_pixel(2, 1)
    hub.light_matrix.set_pixel(3, 1)
    hub.light_matrix.set_pixel(4, 1)
    hub.light_matrix.set_pixel(1, 2)
    hub.light_matrix.set_pixel(5, 2)
    hub.light_matrix.set_pixel(3, 3)
    hub.light_matrix.set_pixel(3, 4)
    hub.light_matrix.set_pixel(3, 5)


def reset_legs():
    front_motor.run_to_position(0)
    back_motor.run_to_position(0)
    steering_motor.run_to_position(0)


distanceSensor = DistanceSensor('B')

while True:
    forward_animation()
    steering_motor.set_default_speed(30)
    steering_motor.run_to_position(0)
    motorPair.set_default_speed(100)
    steering_motor.set_default_speed(20)
    motorPair.start()

    distanceSensor.wait_for_distance_closer_than(30, 'cm')
    hub.light.matris.show.image('GO_LEFT')
    steering_motor.set_default_speed(30)
    steering_motor.run_for_degrees(45)
    motorPair.move(unit='cm', steering=20, speed=40)
    motorPair.stop()
    steering_motor.run_to_position(0)
    reset_legs()
    forward_animation()
    hub.right_button.wait_until_pressed()
    stop(0)
