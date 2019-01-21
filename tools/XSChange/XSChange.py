import os
import sys
from ..utils.PropertiesUtils import PropertiesUtils
from ..utils.FileUtils import FileUtils
PropUtils = PropertiesUtils("C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\XSChange\\config.properties")
FileUtils = FileUtils("C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\XSChange")
def printTips(dict):
	count = 0
	for key in dict:
		print(str(key) + ": " + dict.get(key))
def entry():
	print("*********欢迎使用XSChange*********")
	allType = FileUtils.getAllType()
	printTips(allType)
	while True:
		appType = int(input("请输入应用编号(0：退出)："))
		if appType == 0:
			sys.exit()
		if appType > len(allType) or appType < 0:
			print("您输入的编号有误，请重新输入")
			printTips(allType)
			continue
		break
	allCfg = FileUtils.getTypeCfg(allType.get(appType))
	printTips(allCfg)
	while True:
		cfgType = int(input("请输入配置编号(0：退出)："))
		if cfgType == 0:
			sys.exit()
		if cfgType > len(allCfg) or cfgType < 0:
			print("您输入的编号有误，请重新输入")
			printTips(allCfg)
			continue
		break
	##Start to write configuration
	print("--------------Info Start-------------------")
	print("您选择的应用类型为：" + allType.get(appType) + ", 配置类型为：" + allCfg.get(cfgType))
	desPath = PropUtils.getConfigPath(allType.get(appType))
	sourcePath = FileUtils.getFilePath(allType.get(appType), allCfg.get(cfgType))
	print("DesPath: " + desPath)
	print("SrcPath: " + sourcePath)
	print("--------------Info End---------------------")
	content = FileUtils.readFile(sourcePath)
	FileUtils.writeFile(content, desPath)
	print("设置成功!!!")
	input("请按任意键退出~")
	sys.exit()
	
