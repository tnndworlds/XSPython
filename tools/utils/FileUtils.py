#-*- coding:utf-8 -*-
import os;
class FileUtils(object):
	def __init__(self, cfgDirectory):
		self.props = {}
		self._loadCFG(cfgDirectory)

	def _loadCFG(self, cfgDirectory):
		if not os.path.exists(cfgDirectory):
			print("Error: config directory not exist.")
			return
		for root, dirs, files in os.walk(cfgDirectory):
			for file in files:
				if file.endswith(".cfg"):
					fileName = file[:-4]
					typeCfg = fileName.split("#")
					cfgList = {}
					if typeCfg[0] in self.props:
						cfgList = self.props.get(typeCfg[0])
					cfgList[typeCfg[1]] = root + "\\" + file
					self.props[typeCfg[0]] = cfgList
		
	def readFile(self,cfgPath):
		with open(cfgPath, 'r') as cfgFile:
			return cfgFile.read()

	def writeFile(self, content, writePath):
		with open(writePath, 'w') as _writeFile:
			_writeFile.write(content)

	def getFilePath(self, type, cfg):
		return self.props.get(type).get(cfg)

	def getAllType(self):
		retType = {}
		count = 1
		for key in self.props:
			retType[count] = key
			count = count + 1
		return retType

	def getTypeCfg(self, type):
		retCfg = {}
		count = 1
		for key in self.props.get(type):
			retCfg[count] = key
			count = count + 1
		return retCfg