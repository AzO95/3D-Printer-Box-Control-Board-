#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
from progress.bar import Bar
from colorama import Fore, Back, Style

lights = 11  # lights
printer = 12  # printer

lights_state = 0
printer_state = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(printer, GPIO.OUT)  # printer
GPIO.setup(lights, GPIO.OUT)  # Lights


def board_reboot():
    GPIO.output(printer, GPIO.LOW)  # printer
    printer_state = 0
    GPIO.output(lights, GPIO.LOW)  # lights
    lights_state = 0
    print(Fore.WHITE + ' ---------------------------------------------------------- ')
    print(Fore.RED + ' Reboot de la carte de contrôle! ')
    print(Fore.WHITE + ' ---------------------------------------------------------- ')
    print(Style.RESET_ALL)


bar = Bar('', fill='|', suffix='%(percent)d%%', max=20)

print("")
print(Fore.WHITE + ' 3D PRINTER BOARD SCRIPT ')
print(Fore.RED + ' DISCLAMMER! ')
print(Fore.WHITE + ' ---------------------------------------------------------- ')
print(Fore.RED + ' NOTICE! Do not execute this script this during a 3D print! ')
print(Fore.WHITE + ' Please wait before starting the check! ')
print(Fore.WHITE + ' ---------------------------------------------------------- ')
print(Style.RESET_ALL)

time.sleep(3)
GPIO.output(printer, GPIO.HIGH)  # printer
printer_state = 1
print(Fore.GREEN + 'Check in progress!')
bar.next()
bar.next()
time.sleep(1)
bar.next()
time.sleep(1)
bar.next()
bar.next()
time.sleep(1)
bar.next()
time.sleep(1)
bar.next()
time.sleep(1)
bar.next()
time.sleep(1)
bar.next()
GPIO.output(printer, GPIO.LOW)  # printer
printer_state = 0
bar.next()
bar.next()
time.sleep(1)
bar.next()
GPIO.output(lights, GPIO.HIGH)  # lights
light_state = 1
bar.next()
bar.next()
time.sleep(1)
bar.next()
time.sleep(1)
bar.next()
GPIO.output(lights, GPIO.LOW)  # lights
light_state = 0
bar.next()
bar.next()
bar.next()
bar.next()
time.sleep(2)
print("")
print("")
time.sleep(2)
print(Style.RESET_ALL)

if light_state != 0 and printer_state != 0:
    board_reboot()

else:
    print(Fore.RED + ' Check Is Finished! ')
    print(Fore.WHITE + ' Functions Ok! ')
    print("")
