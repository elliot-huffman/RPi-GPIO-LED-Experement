#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

while True:
    GPIO.output(3, 0)
    time.sleep(1)
    GPIO.output(3, 1)
    time.sleep(1)
GPIO.cleanup()
exit()