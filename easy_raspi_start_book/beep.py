import wiringpi
from time import sleep
import sys
PORT = 18
TONE = 135

wiringpi.wiringPiSetupGpio()
wiringpi.softToneCreate(PORT)

while True:
    try:
        wiringpi.softToneWrite(PORT, TONE)
        sleep(0.5)
        wiringpi.softToneWrite(PORT, 0)
        sleep(0.5)
    except KeyboardInterrupt:
        sys.exit()