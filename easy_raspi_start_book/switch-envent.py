import RPi.GPIO as GPIO
import time

SWITCH = 18
LED = 21
led_value = GPIO.LOW

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
GPIO.setup(LED, GPIO.OUT)

def callback_change_switch(ch):
    global led_value
    print("call back",ch)
    if ch != SWITCH: return
    if led_value == GPIO.LOW:
        GPIO.output(LED, GPIO.HIGH)
        led_value = GPIO.HIGH
    else:
        GPIO.output(LED, GPIO.LOW)
        led_value = GPIO.LOW

GPIO.add_event_detect(
    SWITCH,
    GPIO.RISING,
    callback=callback_change_switch,
    bouncetime=200
)

GPIO.output(LED, GPIO.LOW)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()