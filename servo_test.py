import time
from importlib import reload

from maestro import *

servo_ch = 0            # Servo channel on Maestro board
servo_accel = 50        # Max acceleration (0..255)
servo_speed = 100        # Max speed
servo_pos_begin = 3000  # 0 deg
servo_pos_end = 9000    # 180 deg 

reload(maestro)
servo = maestro.Controller()
servo.setAccel(servo_ch, servo_accel)
servo.setSpeed(servo_ch, servo_speed)
servo.setTarget(servo_ch, servo_pos_begin)

for i in range(3):
    servo.setTarget(servo_ch, servo_pos_end)
    time.sleep(1.0)
    servo.setTarget(servo_ch, servo_pos_begin)
    time.sleep(1.0)