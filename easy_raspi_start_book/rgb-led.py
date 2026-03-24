import RPi.GPIO as GPIO
import time, sys

PORT_R = 17
PORT_G = 27
PORT_B = 22

GPIO.setmode(GPIO.BCM)
ports = [PORT_R, PORT_G, PORT_B]
for port in ports:
    GPIO.setup(port,GPIO.OUT)
    
def set_color(r, g, b):
    GPIO.output(PORT_R, r)
    GPIO.output(PORT_G, g)
    GPIO.output(PORT_B, b)
    
try:
    while True:
        set_color(1, 0, 0)
        print("led")
        time.sleep(0.3)
        set_color(0, 1, 0)
        print("gleen")
        time.sleep(0.3)
        set_color(0, 0, 1)
        print("blue")
        time.sleep(0.3)
except KeyboardInterrupt:
    pass
GPIO.cleanup()