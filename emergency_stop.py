#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

lights = 11  # lights
printer = 12  # printer

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(printer, GPIO.OUT)  # printer
GPIO.setup(lights, GPIO.OUT)  # Lights

GPIO.output(printer, GPIO.LOW)  # printer
GPIO.output(lights, GPIO.LOW)  # lights
