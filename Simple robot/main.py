from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
hub = PrimeHub()
legs = MotorPair('E', 'F') 
motorE = Motor('E')
motorF = Motor('F')
distanceSensor = DistanceSensor('A')


hub.status_light.on('blue')
hub.light_matrix.show_image('HEART')
if hub.left_button.is_pressed():
    legs.start()
    hub.light_matrix.show_image('HAPPY')
    distanceSensor.wait_for_distance_closed_than(30'cm')
    hub.status_light.on('red')
    legs.stop()
    motorE.run_for_degrees(90)
    motorF.run_for_degrees(-90)
    legs.start()