from time import sleep
import wiringpi

PORT = 18
DELAY = 0.5

c = 262
d = 294
e = 330
f = 349
g = 392
a = 470
b = 494
r = 0

gakufu = [
    c,d,e,r, c,d,e,r, g,e,d,c, d,e,d,r,
    c,d,e,r, c,d,e,r, g,e,d,c, d,e,c,r,
    g,g,e,g, a,a,g,r, e,e,d,d, c,r,r,r
]

wiringpi.wiringPiSetupGpio()
wiringpi.softToneCreate(PORT)

for tone in gakufu:
    wiringpi.softToneWrite(PORT, tone)
    sleep(DELAY)
    wiringpi.softToneWrite(PORT, 0)
    sleep(0.1)