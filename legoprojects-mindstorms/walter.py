from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


hub = MSHub()


frontLegs = MotorPair('A', 'B')
rearLegs = MotorPair('E', 'F')
motorA = Motor('A')
motorB = Motor('B')
motorE = Motor('E')
motorF = Motor('F')
distanceSensor = DistanceSensor('D')

def ready():
    stop()
    motorA.run_to_position(180)
    motorB.run_to_postion(0)
    motorE.run_to_position(0)
    motorF.run_to_postion(180)
    hub.light_stauts.on('yellow')

def idle():
    stop()
    frontLegs.run_to_postion(0)
    rearLegs.run_to_postion(0)
    hub.light_matrix.off()
    hub.status_light.on('blue')


def move(n):
    stop()
    ready()
    frontLegs.start(n)
    rearLegs.start(n)
    hub.light_stauts.on('green')
    hub.light_matrix.show_image('GO_UP')

def stop():
    frontLegs.stop()
    rearLegs.stop()
    hub.light_status.on('orange')
    hub.light_matrix.off()

def turnLeft():
    stop()
    hub.light_matrix.show_image('GO_LEFT')
    motorA.run_for_seconds(3, 100)
    motorB.run_for_seconds(3, -100)
    motorE.run_for_seconds(3, 100)
    motorF.run_for_seconds(3, -100)


while True:
    hub.left_button.wait_until_pressed()
    # move(speed)
    move(100)
    distanceSensor.wait_for_distance_closed_than(30, 'cm')
    turnLeft()

    hub.right_button.wait_until_pressed()
    stop()
