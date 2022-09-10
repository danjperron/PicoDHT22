from machine import Pin
from PicoDHT22 import PicoDHT22
import utime

# DHT22 libray is available at
# https://github.com/danjperron/PicoDHT22

dht_sensor=PicoDHT22(Pin(15,Pin.IN,Pin.PULL_UP),dht11=True)
while True:
    T,H = dht_sensor.read()
    if T is None:
        print(" sensor error")
    else:
        print("{}'C  {}%".format(T,H))
    #DHT22 not responsive if delay to short
    utime.sleep_ms(500)

