from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


hub = MSHub()
MotorA = Motor('A')
MotorE = Motor('E')
legs = MotorPair('A', 'E')

# MotorB = Front steering motor
MotorB = Motor('B')

# MotorF = Rear steering motor
MotorF = Motor('F')

distanceSensor = DistanceSensor('D')

def reset_legs():
    MotorA.run_to_position(0)
    MotorE.run_to_position(0)
    MotorB.run_to_position(0)
    MotorF.run_to_position(0)
def reset_steering():
    MotorB.run_to_position(0)
    MotorF.run_to_position(0)
def forward(n):
    reset_steering()
    legs.start(100)
    hub.light_matrix.show_image('GO_UP')
    hub.light_status.on('green')

def turn_left():
    hub.light_matrix.show_image('GO_LEFT')
    hub.light_status.on('yellow')
    MotorB.run_to_postion(45)
    MotorF.run_to_position(-45)
    wait_for_seconds(3)
    reset_steering()

while True:
    reset_legs()
    # forward(speed)
    forward(100)
    distanceSensor.wait_for_distance_closer_than(100, 'cm')
    turn_left()