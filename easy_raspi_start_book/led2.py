#2つのLEDをチカチカするプログラム
#GPIOなどの必要なモジュールを宣言
import RPi.GPIO as GPIO
import time, sys

#GPIOの初期化
GPIO.setmode(GPIO.BCM) #BCMモードに設定

#GPIOのポートをOUTに設定
PORT_L = 4
PORT_R = 17
GPIO.setup(PORT_L, GPIO.OUT)
GPIO.setup(PORT_R, GPIO.OUT)

#ずっと繰り返す
while True:
    try:
        GPIO.output(PORT_L, GPIO.HIGH) #上を点灯
        GPIO.output(PORT_R, GPIO.LOW) #下を消灯
        time.sleep(0.3) #0.3秒待つ
        GPIO.output(PORT_L, GPIO.LOW) #上を消灯
        GPIO.output(PORT_R, GPIO.HIGH) #下を点灯
        time.sleep(0.3) #0.3秒待つ
    except KeyboardInterrupt:
        #Ctrl＋Cが押されたとき
        GPIO.cleanup()
        sys.exit()