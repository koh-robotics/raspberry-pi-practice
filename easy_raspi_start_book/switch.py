#GPIOなどの必要なモジュールを宣言
import RPi.GPIO as GPIO
import time

SWITCH = 18
LED = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.IN )
GPIO.setup(LED,    GPIO.OUT)

GPIO.output(LED, GPIO.LOW)

try:
    while True:
        if (GPIO.input(SWITCH) == GPIO.HIGH):
            print("high")
            GPIO.output(LED, GPIO.HIGH)
        else:
            print("low")
            GPIO.output(LED, GPIO.LOW)
        time.sleep(0.1)
        
except KeyboardInterrupt:
    GPIO.cleanup()