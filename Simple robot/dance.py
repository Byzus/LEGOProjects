from winsound import PlaySound
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
hub = PrimeHub()
legs = MotorPair('E', 'F') 
motorE = Motor('E')
motorF = Motor('F')
motorE.set_default_speed(40)
motorF.set_default_speed(40)
legs.set_default_speed(40)
distanceSensor = DistanceSensor('A')

def rgb_light():
    while True:
        hub.status_light.on('red')
        hub.status_light.on('orange')
        hub.status_light.on('yellow')
        hub.status_light.on('green')
        hub.status_light.on('lime')
        hub.status_light.on('cyan')
        hub.status_light.on('blue')
        hub.status_light.on('purple')
        hub.status_light.on('pink')



hub.light_matrix.show_image('HEART')
if hub.left_button.is_pressed():
    while True:
        rgb_light()
        hub.light_matrix.show_image('HAPPY')
        # You can paste sounds to dance here
        motorE.run_for_degrees(90)
        motorF.run_for_degrees(-90)
        motorE.run_for_degrees(-180)
        motorF.run_for_degrees(180)
        motorE.run_for_degrees(90)
        motorF.run_for_degrees(-90)
        motorE.run_for_degrees(-360)
        motorF.run_for_degrees(360)
        

if hub.right_button.is_pressed():
    motorE.stop()
    motorF.stop()
    hub.light_matrix.show_image('HAPPY')
    