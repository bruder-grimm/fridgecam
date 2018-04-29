#!/usr/bin/env python

from FileHandler import fileHandler
from CameraController import cameraController
from LightSensor import lightSensor
import os
import json

configPath = '../config.json'

with open(configPath) as config_file:    
    config = json.load(config_file)

photoDir 	= '..' + '/' + config["directory"]
pin 		= config["capacitorPin"]
threshold 	= config["brightnessThreshold"]
sleeptimer	= config["adjustmentTime"]

print(photoDir)
print(pin)
print(threshold)
print(sleeptimer)

fileHandleobject	 		= fileHandler(photoDir)
cameraControllerobject 	= cameraController(fileHandleobject, sleeptimer)
cameraobject 				= cameraControllerobject.get_camera()
LightSensorobject 		= lightSensor(pin, threshold)

while True:
	if LightSensorobject.measure() < threshold:
		cameraControllerobject.capture_image_on(cameraobject)
	else:
		pass

		
