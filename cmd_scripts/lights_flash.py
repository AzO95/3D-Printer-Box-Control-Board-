#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

lights = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(lights, GPIO.OUT)

for i in range(0, 3):
GPIO.output(lights, GPIO.HIGH)
time.sleep(0.0500)
GPIO.output(lights, GPIO.LOW)
time.sleep(0.0500)
GPIO.output(lights, GPIO.HIGH)
time.sleep(0.0500)
GPIO.output(lights, GPIO.LOW)
time.sleep(0.0500)
GPIO.output(lights, GPIO.HIGH)
time.sleep(0.0500)
GPIO.output(lights, GPIO.LOW)
time.sleep(0.0500)
GPIO.output(lights, GPIO.HIGH)
time.sleep(0.0500)
GPIO.output(lights, GPIO.LOW)

time.sleep(1.5)
