from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
vacuum = Motor('A')
motorE = Motor('E')
motorF = Motor('F')
motorPair = MotorPair('E', 'F')
distanceSensor = DistanceSensor('B')

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




while True:
    motorPair.set_default_speed(45)
    vacuum.start()
    motorPair.start()
    hub.status_light.on('blue')

    distanceSensor.wait_for_distance_closed_than(30'cm')
    hub.light_matrix.show_image('GO_LEFT')
    motorPair.stop()
    hub.status_light.on('red')
    motorE.run_for_degrees(90)
    motorF.run_for_degrees(-90)
    
    forward_animation()
    motorPair.start()
    hub.status_light.on('blue')
