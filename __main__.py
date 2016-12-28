#!/usr/bin/python
from gpiozero import Button
from signal import pause
from os import system

button = Button(3)

def pressed(button):
	system('shutdown -h now')

button.when_pressed = pressed

pause()
