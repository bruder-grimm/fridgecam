import picamera
import time

class cameraController(object):
	"""This is for getting a camera instance and capturing pictures on it"""
	def __init__(self, fileHandler, sleepTimer):
		self.fileHandler = fileHandler
		self.sleepTimer = sleepTimer
	
	def capture_image_on(self, camera):
		time.sleep(self.sleepTimer)
		time.sleep(2)
		fileName = self.fileHandler.get_next_filename()
		print(fileName)
		camera.capture(fileName)

		time.sleep(1)

	def get_camera(self):
		camera = self.__apply_camera_properties_to(picamera.PiCamera())
		return camera


	def __apply_camera_properties_to(self, PiCamera):
		# tinker with the properties later when you
		# can actually try the cam in the fridge
	
		# PiCamera.resolution = (2592, 1944)
		# PiCamera.sharpness = 0
		# PiCamera.contrast = 0
		# PiCamera.brightness = 50
		# PiCamera.saturation = 0
		# PiCamera.ISO = 0
		# PiCamera.video_stabilization = False
		# PiCamera.exposure_compensation = 0
		# PiCamera.exposure_mode = 'auto'
		# PiCamera.meter_mode = 'average'
		# PiCamera.awb_mode = 'auto'
		# PiCamera.image_effect = 'none'
		# PiCamera.color_effects = None
		PiCamera.rotation = 90
		# PiCamera.hflip = False
		# PiCamera.vflip = False
		# PiCamera.crop = (0.0, 0.0, 1.0, 1.0)

		return PiCamera
