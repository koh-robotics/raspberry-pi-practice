#LEDをチカチカするプログラム

#GPIOなど必要なモジュールを宣言
import RPi.GPIO as GPIO #GPIOを利用する
import time             #sleepを利用する

PNO = 4 #対象のGPIOポート番号

#GPIOの初期化
GPIO.setmode(GPIO.BCM) #BCMモードに設定
GPIO.setup(PNO, GPIO.OUT) #指定ポートをOUTに設定

#10回繰り返す
for i in range(10):
    print("i=",i)
    GPIO.output(PNO, GPIO.HIGH) #点灯
    time.sleep(0.3) #0.3秒待つ
    GPIO.output(PNO, GPIO.LOW) #消灯
    time.sleep(0.3) #0.3秒待つ

#クリーンアップ
GPIO.cleanup()