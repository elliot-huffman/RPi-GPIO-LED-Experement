#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(2, GPIO.OUT)

while True:
    GPIO.output(2, 0)
    time.sleep(1)
    GPIO.output(2, 1)
    time.sleep(1)
exit()