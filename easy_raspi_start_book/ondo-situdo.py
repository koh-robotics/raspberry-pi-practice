from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
import dht11

PIN = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

dht11_obj = dht11.DHT11(pin=PIN)

for i in range(10):
    while True:
        res = dht11_obj.read()
        if not res.is_valid():
            print("-error:", res)
            sleep(0.1)
            continue
        break
    print("+", datetime.now().strftime('%H:%M:%S'))
    print("| 湿度=",res.humidity,"%")
    print("| 温度=",res.temperature,"度")
    sleep(10)