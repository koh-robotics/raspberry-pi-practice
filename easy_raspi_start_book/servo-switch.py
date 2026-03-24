import RPi.GPIO as GPIO
from time import sleep

SV_PORT = 18
SW1_PORT = 20
SW2_PORT = 21

SV_FREQ = 50 #20ms(50Hz)
SV_DUTY_OFFSET = 0.025
SV_DUTY_RES = (2.4 - 0.5) / 20 / 180

GPIO.setmode(GPIO.BCM)
GPIO.setup(SV_PORT, GPIO.OUT)
GPIO.setup([SW1_PORT, SW2_PORT],
    GPIO.IN,
    pull_up_down=GPIO.PUD_DOWN)

servo = GPIO.PWM(SV_PORT,SV_FREQ)
servo.start(0)
sleep(0.3)

def set_angle(angle):
    if angle < -90: angle = -90
    if angle > 90: angle = 90
    degree = (angle + 90)
    duty = (SV_DUTY_OFFSET + SV_DUTY_RES * degree) * 100
    print("angle=",angle,"duty=",int(duty))
    servo.ChangeFrequency(SV_FREQ)
    servo.ChangeDutyCycle(duty)
    
angle = 0
set_angle(angle)
while True:
    try:
        if GPIO.input(SW1_PORT) == GPIO.HIGH:
            angle -= 2
            set_angle(angle)
        if GPIO.input(SW2_PORT) == GPIO.HIGH:
            angle += 2
            set_angle(angle)
        sleep(0.01)
    except KeyboardInterrupt:
        break
    
GPIO.cleanup()




