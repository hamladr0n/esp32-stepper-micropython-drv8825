# This file is executed on every boot (including wake-boot from deepsleep)
#esp.osdebug(None)
import uos, machine
import webrepl
import mywifi

try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'enter your SSID'
password = 'enter wifi pass'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)
