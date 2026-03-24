import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import dht11

PORT_DHT = 4

PORT_R = 21
PORT_G = 20
PORT_B = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

dht11_obj = dht11.DHT11(pin=PORT_DHT)

ports = [PORT_R, PORT_G, PORT_B]
for port in ports:
    GPIO.setup(port, GPIO.OUT)

def set_color(r, g, b):
    GPIO.output(PORT_R, r)
    GPIO.output(PORT_G, g)
    GPIO.output(PORT_B, b)

try:
    while True:
        print("情報取得中..")
        res = dht11_obj.read()
        if not res.is_valid():
            print("- error:", res)
            sleep(0.1)
            continue
        print("| 湿度=",res.humidity, "%")
        print("| 温度=",res.temperature, "度")

        t = res.temperature
        if t < 10:
            set_color(0, 0, 1)
        elif 10 <= t < 15:
            set_color(0, 1, 0)
        elif 15 <= t < 20:
            set_color(1, 1, 1)
        elif 20 <= t <25:
            set_color(1, 0, 1)
        else:
            set_color(1, 0, 0)
        sleep(10)
except Exception as e:
    print(e)
    pass
GPIO.cleanup()