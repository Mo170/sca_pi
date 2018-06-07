#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

touch_pin=31
led_pin = 11

GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(touch_pin,GPIO.OUT)

while True:
    if GPIO.input(touch_pin) == 0:
        GPIO.output(led_pin,False)
        time.sleep(2)
    if GPIO.input(touch_pin) == 1:
        GPIO.setup(led_pin,True)
        time.sleep(2)
        GPIO.cleanup()        
            
