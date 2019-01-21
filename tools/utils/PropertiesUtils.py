#-*- coding:utf-8 -*-
import os;
class PropertiesUtils(object):
	def __init__(self, fileName):
		self.fileName = fileName
		self.props = {}
		try:
			cfgFile = open(fileName, 'r')
			self._init_props(cfgFile)
		finally:
			if cfgFile:
				cfgFile.close()

	def _init_props(self, cfgFile):
		for line in cfgFile.readlines():
			line = line.strip().replace('\n', '')
			if line.find("#") != -1:
				continue
			if line.find("=") > 0:
				keyValue = line.split("=")
				self.props[keyValue[0]] = keyValue[1]

	def getConfigPath(self, type):
		return self.props.get(type).format(userId=os.getlogin())
