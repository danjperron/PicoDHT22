from machine import Pin
from esp32_gpio_lcd import GpioLcd
from DHT22 import DHT22
import time

# P.S.
# GpioLcd Library is available at
# https://github.com/dhylands/python_lcd
# you need to copy the files esp32_gpio_lcd.py and lcd_api.py into the Pico.
#
# DHT22 libray is available at
# https://github.com/danjperron/PicoDHT22


# init LCD 1602  (4 bits mode)
lcd = GpioLcd(rs_pin=Pin(0), rw_pin=Pin(1), enable_pin=Pin(2),
              d4_pin=Pin(4), d5_pin=Pin(5), d6_pin=Pin(6),d7_pin=Pin(7))
# day of the week in French
jour = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]

# init DHT22 on Pin 15
dht22 = DHT22(Pin(15,Pin.IN,Pin.PULL_UP))
lcd.clear()
while True:
    T, H = dht22.read()
    now = time.localtime()
    lcd.putstr("{} {:02}  {:02d}:{:02d}:{:02d}".format(jour[now[6]],
                                                      now[2],now[3],
                                                      now[4],now[5]))
    lcd.move_to(0,1)

    if T is None:
        lcd.putstr("T=----\xdfC H=----}%")
    else:
        lcd.putstr("T={:3.1f}\xdfC H={:3.1f}%".format(T,H))
    time.sleep_ms(500)

