from machine import Pin
import time 

dp = Pin(4, Pin.OUT) # d2 wemos # DIR pin
sp = Pin(5, Pin.OUT) # d1 wemos # STEP pin
#ep = Pin(2, Pin.OUT) #d4 wemos

dp.value(0)  # DIR pin
sp.value(0)  # STEP pin

#class step():
#    def __init__():
#        pass
    
def forward():
    dp.value(1)
    for i in range(1000):
        sp.value(1)
        time.sleep_us(500)
        sp.value(0)
        print(i)
        time.sleep_us(500)

def back():
    dp.value(0)
    for i in range(1000):
        sp.value(1)
        time.sleep_us(500)
        sp.value(0)
        print(i)
        time.sleep_us(500)

