#!/usr/bin/env python

import random
i = 0 
num_random_numbers = 100
while i < num_random_numbers:
    random_number = random.randint(1,100)
    guessed_number =int(raw_input("guess an integer (between 1 and 100): "))
    print "random number is", random_number
    if guessed_number != random_number:
        print "Your guess was not correct. please try again."
    i = i + 1
