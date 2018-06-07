#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 225)
black = (0, 0, 0)

speed = 0.01
message = "Hello World!"
guess = " "
while guess != message:
    sense.show_message(message, speed, text_colour=yellow, back_colour=black)
    guess = raw_input("what is your guess?")
    speed = speed + 0.005

print "congrats you win"

sense.clear()
