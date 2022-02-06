import time
import RPi.GPIO as GPIO
from .maestro import *
from importlib import reload

from mycroft import MycroftSkill, intent_file_handler

# Settings
led_pin = 18            # Physical pin 12
servo_ch = 0            # Servo channel on Maestro board
servo_accel = 50        # Max acceleration (0..255)
servo_speed = 100       # Max speed
servo_pos_begin = 3000  # 0 deg
servo_pos_end = 9000    # 180 deg 

# Skill class that inherits from MycroftSkill
class RoboInteract(MycroftSkill):

    # Constructor
    def __init__(self):
        MycroftSkill.__init__(self)
        
        # Set up LED
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led_pin, GPIO.OUT)
        
        # Set up servo controller
        reload(maestro)
        self.servo = maestro.Controller()
        self.servo.setAccel(servo_ch, servo_accel)
        self.servo.setSpeed(servo_ch, servo_speed)
        self.servo.setTarget(servo_ch, servo_pos_begin)
        
    # Called after skill loads
    def initialize(self):
        self.log.info("Robo interact skill loaded")

    # Called whenever skill is activated
    @intent_file_handler('interact.robo.intent')
    def handle_interact_robo(self, message):
    
        # Get string value from 'action' variable
        action = message.data.get('action')
        
        # Do a blink
        if action.casefold() == "blink":
            self.log.info("Blinking!")
            self.speak_dialog('interact.robo', data={
                'action': action
            })
            for i in range(2):
                GPIO.output(led_pin, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(led_pin, GPIO.LOW)
                time.sleep(0.5)
        
        # Do a wave
        elif action.casefold() == "wave":
            self.log.info("Waving!")
            self.speak_dialog('interact.robo', data={
                'action': action
            })
            self.servo.setTarget(servo_ch, servo_pos_end)
            time.sleep(1.0)
            self.servo.setTarget(servo_ch, servo_pos_begin)
        
        # Unsupported action
        else:
            self.log.info("No can do")
            self.speak_dialog('negative.interact.robo')

# Called by Mycroft to create skill object
def create_skill():
    return RoboInteract()

