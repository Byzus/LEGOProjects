from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike import MotorPair
from math import *

hub = PrimeHub()

hub.light.off()
hub.speaker.beep()

motorPair = MotorPair('E', 'F')
