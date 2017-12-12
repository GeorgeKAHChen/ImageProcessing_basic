#=================================================================
#
#		Image Processing - ImgEnp.py
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
import random 

#import files
import Init
import Convolution


def GetEnp(img):
	Pixel = [0 for n in range(260)]
	Prob = [0.00 for n in range(260)]
	TTL = 0
	for i in range(0, len(img)):
		for j in range(0, len(img)):
			Pixel[img[i][j]] += 1
			TTL += 1

	for i in range(0, len(Prob)):
		Prob[i] = Pixel[i] / TTL

	Entropy = 0.00
	for i in range(0, len(Prob)):
		if Prob == 0:
			continue
		else:
			Entropy += Prob[i] * math.log(Prob[i], 2)


def MET(img):
	METi = 0
	METSum = -99999.00
	Sum = [0 for n in range(260)]
	Pro = [0.000 for n in range(260)]
	ProSum = [0.000 for n in range(260)]
	TTL = len(img) * len(img[0])

	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			Sum[int(img[i][j])] += 1

	for i in range(0, len(Sum)):
		Pro[i] = Sum[i] / TTL
		if i != 0:
			ProSum[i] = ProSum[i-1] + Pro[i]
		else:
			ProSum[i] = Pro[i]

	for i in range(0, len(ProSum)):
		Ent = 0
		for j in range(0, len(Pro)):
			if Pro[j] == 0:
				continue
			if j <= i:
				Ent -= (Pro[j]/ProSum[i] * math.log(Pro[j]/ProSum[i]+0.001))
			else:
				Ent -= (Pro[j]/(1-ProSum[i]) * math.log(Pro[j]/(1-ProSum[i])+0.001))

		if Ent > METSum:
			METi = i
			METSum = Ent

	print("argmax = " + str(METi))
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			if img[i][j] <= METi:
				img[i][j] = 0
			else:
				img[i][j] = 255


def Main(img):
	print(GetEnp(img))
	print(GetEnp(MET(img)))



