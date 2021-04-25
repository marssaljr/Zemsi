#!/usr/bin/python3

import sys, shutil, os
import subprocess
from os import path, listdir

launcher = "Wow.exe -opengl"
home = path.expanduser("~")

class startWOW:
	def __init__(self, launcher, home, source_data):
		self.launcher = launcher
		self.source_data = source_data
		self.startProcess(home)

	def findIt(self):
		for file in listdir("./"):
			dirnames = path.join("./", file)
			if path.isdir(dirnames):
				d = dirnames.replace("./", "").split()
				for name in d:
					if path.exists(name+"/Data"):
						return name
#
	def changeDir(self, dados):
		try:
			shutil.move(dados, self.source_data)
			print(self.source_data + " Agora contém os arquivos")
		except shutil.Error as err:
			print(err)
			print("Já contém os arquivos")
		return True

	def startProcess(self, home):
		dirname = str(self.findIt())
		dados = home + "/wow/" + dirname + "/Data"
		caminho = dados + "/Data/"

		if (self.changeDir(dados) == True):
			try:
				os.system("wine " + self.source_data + self.launcher)
			except:
				print("Erro at try start")
		else:	
			print("Erro at startProcess")

if (len(sys.argv) > 1):
	source_data = home + "/wow/" + sys.argv[1] + "/"
	startWOW(launcher, home, source_data)
else:
	print("""Favor informar o nome da pasta do server:
	ex: python3 wow.py pandawow
	""")
	exit(1)
