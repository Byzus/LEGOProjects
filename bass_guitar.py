from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
hub.status_light.on('white')

forceSensor = ForceSensor('A')
colorSensor = ColorSensor('B')

# Note that you can always change sound and colors
if forceSensor.is_pressed():
    colorSensor = ColorSensor('B')

    colorSensor.wait_until_color('red')
    hub.status_light.on('red')
    hub.speaker.beep(40, 0.5)
    hub.status_light.on('white')

    colorSensor.wait_until_color('yellow')
    hub.status_light.on('yellow')
    hub.speaker.beep(50, 0.5)
    hub.status_light.on('white')

    colorSensor.wait_until_color('green')
    hub.status_light.on('green')
    hub.speaker.beep(60, 0.5)
    hub.status_light.on('white')

    colorSensor.wait_until_color('blue')
    hub.status_light.on('blue')
    hub.speaker.beep(70, 0.5)
    hub.status_light.on('white')

