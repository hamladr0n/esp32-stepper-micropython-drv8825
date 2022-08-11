from machine import Pin  
import time

# dir = pin 12  (d6 on esp8266 - GPIO 12)
# step = pin 14 (d5 on esp8266 - GPIO 14)
# enable = pin 13 (d7 on esp8266 - GPIO 13)

dp = Pin(4, Pin.OUT) # d2 wemos
sp = Pin(5, Pin.OUT) # d1 wemos
ep = Pin(2, Pin.OUT) #d4 wemos 

ep.value(1)
dp.value(1)
sp.value(1)

ep.value(0)
for i in range(1000):
    sp.value(1)
    time.sleep_us(2)
    sp.value(0)
    print(i)
    time.sleep_us(1000)

