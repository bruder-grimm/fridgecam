import os
import fnmatch

class fileHandler(object):
	"""for establishing folders exist and so"""
	def __init__(self, path):
		self.path = path
		self.fileCount = -1
		self.__prepare_file_path()

	def get_next_filename(self):
		self.fileCount += 1
		return self.path + '/' + "fridge_photo_%s.jpg" % self.fileCount

	def __prepare_file_path(self):
		if not os.path.isdir(self.path):
			os.makedirs(self.path)
			print("created path %s" % self.path)
		if self.fileCount < 0:
			self.fileCount = len(fnmatch.filter(os.listdir(self.path), '*.jpg'))
		print("using %s as path for captured images" % self.path)
		print("%s files present in folder" % self.fileCount)
