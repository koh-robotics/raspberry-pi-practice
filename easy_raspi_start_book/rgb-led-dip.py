import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BCM)

PORT_R = 17
PORT_G = 27
PORT_B = 22

DIP1 = 5
DIP2 = 6
DIP3 = 13

ports = [PORT_R, PORT_G, PORT_B]
for port in ports:
    GPIO.setup(port, GPIO.OUT)
dips = [DIP1, DIP2, DIP3]
for port in dips:
    GPIO.setup(port, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def set_color(r, g, b): 
     GPIO.output(PORT_R, r)
     GPIO.output(PORT_G, g)
     GPIO.output(PORT_B, b)
     print(r, g, b)
     
try:
    while True:
        r = g = b = GPIO.LOW
        if GPIO.input(DIP1) == GPIO.LOW:
            r = GPIO.HIGH
        if GPIO.input(DIP2) == GPIO.LOW:
            g = GPIO.HIGH
        if GPIO.input(DIP3) == GPIO.LOW:
            b = GPIO.HIGH
        set_color(r, g, b)
        time.sleep(0.3)
except KeyboardInterrupt:
    pass
GPIO.cleanup()