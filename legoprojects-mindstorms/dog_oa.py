from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
# Check the robot tutorial : https://www.youtube.com/watch?v=8vQnB-2ZK6M&t=13s
# To build robot you need 1 lego mindstorms 51515 kit.
dog = MSHub()
legs = MotorPair('A','B')
Lleg = Motor('A')
Rleg = Motor('B')
dsensor = DistanceSensor('D')
# Head motors are for head movement that I built. You can build your own attachments and change the code.
head_up = Motor('E')
head_steer = Motor('F')
dog.speaker.beep()
legs.set_default_speed(50)
def calibrate():
    Lleg.run_to_position(0)
    Rleg.run_to_position(0)
    head_up.run_to_position(0)
    head_steer.run_to_position(0)
while True:
    calibrate()
    dog.speaker.beep()
    legs.start(0, 50)
    dsensor.wait_for_distance_closer_than(20, 'cm')
    legs.stop()
    legs.start(-100, 50)
    wait_for_seconds(3)
    legs.stop()
    legs.start(0, 50)
# This program is tested and it's working on lego 51515 robot inventor hub.
# You can copy this program and paste it to the lego mindstorms robot inventor app.