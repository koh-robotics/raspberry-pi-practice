import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 100000

def abc_reead10(ch):
    r = spi.xfer2([1,(8 + ch << 4), 0])
    v = ((r[1] & 3) << 8) + r[2]
    return v