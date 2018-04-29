import RPi.GPIO as GPIO
import time
import picamera

from timeit import default_timer as timer

class lightSensor(object):
	"""senses things, mostly light"""
	def __init__(self, capacitorPin, brightnessThreshold):
		# set the pinout of the gpio to BCM, since I have no
		# Idea what the other pinout looks like and the 
		# documentation is seriously... just.. not
		GPIO.setmode(GPIO.BCM)
		self.capacitorPin = capacitorPin
		self.brightnessThreshold = brightnessThreshold

	def is_fridge_open(self):
		if self.measure() < self.brightnessThreshold:
			return False
		else:
			return True
	
	def measure(self):
		pin = 4
		GPIO.setmode(GPIO.BCM)
  		GPIO.setup(pin, GPIO.OUT)
  		GPIO.output(pin, GPIO.LOW)

  		time.sleep(0.1)
  		GPIO.setup(pin, GPIO.IN)
  		measurement = 0
  		while(GPIO.input(pin) == GPIO.LOW):
    			measurement += 1
		print measurement

 	 	return measurement

	def __measure_light(self):
		self.__discharge_capacitor(self.capacitorPin)
		start = timer()

		self.__charge_capacitor(self.capacitorPin)
		end = timer()

		bValue = end - start
		print(bValue)

		return bValue

	def __discharge_capacitor(self):
		GPIO.setup(self.capacitorPin, GPIO.OUT)
		GPIO.output(self.capacitorPin, GPIO.LOW)
		time.sleep(0.1)

	def __charge_capacitor(self):
		GPIO.setup(self.capacitorPin, GPIO.IN)
		while (GPIO.input(self.capacitorPin)) == GPIO.LOW:
			pass

