#!/usr/bin/env python
from sense_hat import SenseHat
import time 
import random 
sense = SenseHat()

a=raw_input("write a message")
for c in a:
    sense.show_letter(c, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    time.sleep(1)
sense.clear()
