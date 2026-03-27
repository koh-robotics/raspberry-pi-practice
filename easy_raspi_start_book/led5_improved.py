#5つのLEDを光らせるプログラム
#GPIOなどの必要なモジュールを宣言
import RPi.GPIO as GPIO
import time, sys

#GPIOの初期化
GPIO.setmode(GPIO.BCM) #BCMモードに設定
#各ポートをOUTに設定
ports = [5,6,13,19,26];
for i in ports:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
    
#特定箇所のポートだけを光らせる
def led_on(no):
    for i, port in enumerate(ports):
        if no == i:
            v = GPIO.HIGH
        elif 4 - no == i:
            v = GPIO.HIGH
        else:
            v = GPIO.LOW
        GPIO.output(port, v)
def led_time(ti):
    if ti == 2:
        time.sleep(0.05)
    else:
        time.sleep(0.1)
        
#ずっと繰り返す
while True:
    try:
        for i in range(0, 5):
            led_on(i)
            led_time(i) #待つ
        for i in range(4, -1, -1):
            led_on(i)
            led_time(i) #待つ
    except KeyboardInterrupt:
        # Ctrl+Cが押されたとき
        GPIO.cleanup()
        sys.exit()
        