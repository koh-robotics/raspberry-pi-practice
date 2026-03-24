import RPi.GPIO as GPIO
from time import sleep 
import sys

SOUND_PORT = 18
TONE = 440
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_PORT, GPIO.OUT)

pwm = GPIO.PWM(SOUND_PORT, TONE)

while True:
    try:
        pwm.ChangeFrequency(TONE)
        pwm.start(50)
        sleep(0.5)
        pwm.stop()
        sleep(0.5)
    except KeyboardInterrupt:
        break

GPIO.cleanup()
sys.exit()