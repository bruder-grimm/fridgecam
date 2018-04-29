#!/usr/bin/env python

import RPi.GPIO as GPIO, time

f = open('iawdawdnsidefridge.txt', 'w')

GPIO.setmode(GPIO.BCM)
for i in range(400):
  pin = 4

  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.LOW)

  time.sleep(0.1)
  GPIO.setup(pin, GPIO.IN)
  measurement = 0
  while(GPIO.input(pin) == GPIO.LOW):
    measurement += 1

  print >> f, measurement

f.close()
