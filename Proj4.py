#=================================================================
#
#		Image Processing - Proj4
#		Copyright(c) KazukiAmakawa, all right reserved.
#
#=================================================================
#import head
from copy import deepcopy
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
import math
import matplotlib.patches as patches
from collections import deque

#import files
import Init

def PDEMethod(img, kind):
	imgSave = img
	img1 = [[0 for n in range(len(img[1]))] for n in range(len(img))]
	VarN = 24

	#Linear
	Lambda = 10
	delta_t = 0.1
	"""
	if kind == 2:
		Lambda = Init.IntInput("Now input the lembda you need:  ", "0", "99999", "float")
		delta_t = Init.IntInput("Now input the lembda you delta_t:  ", "0", "99999", "float")
	"""
	def g(x):
		return float(pow(2.71828, (- (x * x) / (2 * Lambda * Lambda) )))
	
	#Non-Linear
	Variable = 0.1

	#MainLoop
	for k in range(0 ,VarN):
		print([k, VarN])
		for i in range(0, len(img)):
			for j in range(0, len(img[i])):
				tem = []
				try:
					tem.append(imgSave[i-1][j])
				except:
					tem.append(0)
				try:
					tem.append(imgSave[i+1][j])
				except:
					tem.append(0)
				try:
					tem.append(imgSave[i][j-1])
				except:
					tem.append(0)
				try:
					tem.append(imgSave[i][j+1])
				except:
					tem.append(0)

				if kind == 1:
					#Linear Method
					img1[i][j] = imgSave[i][j] + Variable * (tem[0] + tem[1] + tem[2] + tem[3] - 4 * imgSave[i][j])
				else:
					#Non-linear Method
					Additem = 0
					Additem += g(abs(tem[3] - imgSave[i][j])) #* (tem[3] - imgSave[i][j])
					Additem -= g(abs(tem[2] - imgSave[i][j])) #* (tem[2] - imgSave[i][j])
					Additem += g(abs(tem[1] - imgSave[i][j])) #* (tem[1] - imgSave[i][j])
					Additem -= g(abs(tem[0] - imgSave[i][j])) #* (tem[0] - imgSave[i][j])
					img1[i][j] = imgSave[i][j] + delta_t * Additem
		imgSave = deepcopy(img1)

	for i in range(0, len(imgSave)):
		for j in range(0, len(imgSave[i])):
			imgSave[i][j] = int(imgSave[i][j])
			imgSave[i][j] = min(255, imgSave[i][j])
			imgSave[i][j] = max(0, imgSave[i][j])
	return imgSave
