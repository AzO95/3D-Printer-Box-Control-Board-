#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

lights = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(lights, GPIO.OUT)

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
time.sleep(0.0500)

time.sleep(1.5)
