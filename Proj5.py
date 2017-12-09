#=================================================================
#
#		Image Processing - Proj5
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

#Constant Definition
Lambda = 0.001
#For the LSE function

VarN = 20
#For the iterative times

Alpha = 0.01
#For the IS Method

def LSE(img):
	Kernel = np.matrix([[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4],[1, 4, 7, 4, 1]]) / 273
	bluredim = Convolution.D2FFT(img, Kernel)
	"""
	for i in range(0, 100):
		LocX = random.randint(0, len(img[0]-2))
		LocY = random.randint(0, len(img-2))
		Var = random.randint(-255, 255)
		bluredim[LocX][LocY] += Var
		bluredim[LocX][LocY] = min(255, int(bluredim[LocX][LocY]))
		bluredim[LocX][LocY] = max(0, int(bluredim[LocX][LocY]))
	"""
	return bluredim
	H = np.matrix(np.fft.fft2(img))
	HT = H.transpose()
	HTH = HT * H
	g = np.fft.fft2(bluredim)
	
	EHT = np.matrix([[0 for n in range(max( len(HT[0]), len(g[0]) ))] for n in range(max( len(HT), len(g) ))])
	Eg = np.matrix([[0 for n in range(max( len(HT[0]), len(g[0]) ))] for n in range(max( len(HT), len(g) ))])
	for i in range(0, len(EHT)):
		for j in range(0, len(EHT[i])):
			try:
				EHT[i][j] = HT[i][j]
			except:
				EHT[i][j] = 0

			try:
				Eg[i][j] = HTH[i][j]
			except:
				Eg[i][j] = 0

	HTg = EHT * Eg 
	HTH += Lambda
	HTHI = HTH.I 
	
	EHTg = np.matrix([[0 for n in range(max( len(HTH[0]), len(HTg[0]) ))] for n in range(max( len(HTH), len(HTg) ))])
	EHTH = np.matrix([[0 for n in range(max( len(HTH[0]), len(HTg[0]) ))] for n in range(max( len(HTH), len(HTg) ))])
	for i in range(0, len(EHTg)):
		for j in range(0, len(EHTg[i])):
			try:
				EHTg[i][j] = HTg[i][j]
			except:
				EHTg[i][j] = 0

			try:
				EHTH[i][j] = HTH[i][j]
			except:
				EHTH[i][j] = 0

	f = np.fft.ifft2(EHTg * EHTH.I).real

	for i in range(0, len(f)):
		for j in range(0, len(f[i])):
			f[i][j] = min(255, int(f[i][j]))
			f[i][j] = max(0, int(f[i][j]))

	return f


def ISCal(img):
	img = np.matrix(img)
	H = np.matrix(np.fft.fft2(img))
	HT = H.transpose()

	Kernel = np.matrix([[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4],[1, 4, 7, 4, 1]]) / 273
	bluredim = Convolution.D2FFT(img, Kernel)
	"""
	for i in range(0, 100):
		LocX = random.randint(0, len(img[0]-2))
		LocY = random.randint(0, len(img-2))
		Var = random.randint(-255, 255)
		bluredim[LocX][LocY] += Var
		bluredim[LocX][LocY] = min(255, int(bluredim[LocX][LocY]))
		bluredim[LocX][LocY] = max(0, int(bluredim[LocX][LocY]))
	"""
	H = np.matrix(np.fft.fft2(img))
	HT = H.transpose()
	HTH = HT * H
	g = np.fft.fft2(bluredim)
	
	EHT = np.matrix([[0.00 for n in range(max( len(HT[0]), len(g[0]) ))] for n in range(max( len(HT), len(g) ))])
	Eg = np.matrix([[0.00 for n in range(max( len(HT[0]), len(g[0]) ))] for n in range(max( len(HT), len(g) ))])
	for i in range(0, len(EHT)):
		for j in range(0, len(EHT[i])):
			try:
				EHT[i][j] = HT[i][j]
			except:
				EHT[i][j] = 0

			try:
				Eg[i][j] = HTH[i][j]
			except:
				Eg[i][j] = 0

	HTg = EHT * Eg 
	EHTH = EHT * EHT.transpose()
	EHTH = EHTH + Lambda
	return img + Alpha * (EHTg - EHTH * img)


def IS(img):
	for i in range(0, VarN):
		Kernel = np.matrix([[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4],[1, 4, 7, 4, 1]]) / 273
		img = Convolution.D2FFT(img, Kernel)
		if VarN:
			return img
		else:
			img = ISCal(img)
	return img






