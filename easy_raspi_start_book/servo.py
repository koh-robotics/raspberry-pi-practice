import RPi.GPIO as GPIO
from time import sleep

SV_PORT = 18
SV_FREQ = 50
SV_DUTY_OFFSET = 0.025
SV_DUTY_RES = (2.4 - 0.5) / 20 / 180

GPIO.setmode(GPIO.BCM)
GPIO.setup(SV_PORT, GPIO.OUT)
servo = GPIO.PWM(SV_PORT,SV_FREQ)
servo.start(0)

def set_angle(angle):
    degree = angle + 90
    duty = (SV_DUTY_OFFSET + SV_DUTY_RES * degree) * 100
    print("angle=",angle,"duty=", int(duty))
    servo.ChangeFrequency(SV_FREQ)
    servo.ChangeDutyCycle(duty)
    
while True:
    try:
        set_angle(90)
        sleep(1)
        
        set_angle(0)
        sleep(1)
        
        set_angle(-90)
        sleep(1)
        
        set_angle(0)
        sleep(1)
    except KeyboardInterrupt:
        break
    
GPIO.cleanup()