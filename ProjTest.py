#=================================================================
#
#		Image Processing - Main
#		Copyright(c) KazukiAmakawa, all right reserved.
#
#=================================================================
#This is the main function of the program, all program will begin from this program
#May cannot compile under the Windows System.

#import head
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
import math
import matplotlib.patches as patches
from scipy import misc
from collections import deque
from PIL import ImageFilter
import cv2
import random
import pywt 
from copy import deepcopy
import time


#import files
import Init


#Definition Constant
Beta = 0.1
Lambda = 0.1 
Gamma = 0.04
TotalKase = 3

def Wavelet(img):
	img1 = np.array([[np.float64(0.00) for n in range(len(img[0]))] for n in range(len(img))])
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img1[i][j] = float(img[i][j])
	coeffs = pywt.dwt2(img1, "haar")
	#Init.ArrOutput(coeffs)
	return pywt.idwt2(coeffs, "haar")


def Gauss(img):
	Rem = [[0 for n in range(len(img[0]) + 20)] for n in range(len(img) + 20)]
	img = cv2.GaussianBlur(img, (11, 11), 1.6)
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			rand = random.normalvariate(0, 1.4142135623730951)
			img[i][j] += rand
			Rem[i][j] += rand
	Wavelet(img)
	return img, Rem


def ADMM(img):
	#Pre-treatment
	img, Rem = Gauss(img)
	Jud = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	#print(img)
	#print(Rem)
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = float(img[i][j])
			Rem[i][j] = float(Rem[i][j])
	#Definition Iterator vartiables
	u = np.matrix(img)
	y = [[0.00 for n in range(0, len(img[0]))] for n in range(len(img))]
	y = np.matrix(pywt.dwt2(y, "haar"))
	mu = [[0.00 for n in range(0, len(img[0]))] for n in range(len(img))]
	mu = np.matrix(pywt.dwt2(mu, "haar"))
	"""
	for i in range(0, len(y)):
		for j in range(0, len([i])):
			print(y[i][j])
	"""
	#y = [np.matrix(y[0]), np.matrix(y[1]), np.matrix(y[2]), np.matrix(y[3])]
	#mu = [np.matrix(mu[0]), np.matrix(mu[1]), np.matrix(mu[2]), np.matrix(mu[3])]

	#Definition Constant
	H = np.matrix(np.abs(np.fft.fftshift(np.fft.fft2(img).real)))
	
	HT = H.transpose()

	#Main Algorithm
	for Kase in range(0, TotalKase):
		if TotalKase == 0:
			#print(TotalKase)
			u1 = ((np.matrix(H.transpose() * H) + Beta).I) * (HT * u + Beta * np.matrix(pywt.idwt2([y[0] + mu/Beta, y[1] + mu/Beta, y[2] + mu/Beta, y[3] + mu/Beta], "haar")))
			#print("SB!!")
			#y1 = pywt.dwt2(u1) - mu/Beta
			y1 = y
			if Gamma < 1:
				#print("Input Error")
				time.sleep(5)
				break
			if np.abs(y1.all()) > 0.0001:
				y1 -= Lambda / Beta
			elif np.abs(y1.all()) < 0.0001:
				y1 += Lambda / Beta
			else:
				y1 = np.matrix([[0.00 for n in range(0, len(img[0]))] for n in range(len(img))] for n in range(4))
			
			mu1 = mu + Gamma*(y1 - pywt.dwt2(u1))

			u = u1
			y = y1
			mu = mu1
		
		else:
			pass

		for i in range(0, len(img)):
			for j in range(0, len(img[i])):
				Jud[i][j] = img[i][j] - 0.1*Rem[i][j]

	#After treatment
	for i in range(0, len(Jud)):
		for j in range(0, len(Jud[i])):
			Jud[i][j] = int(Jud[i][j])
			Jud[i][j] = min(255, Jud[i][j])
			Jud[i][j] = max(0, Jud[i][j])


	return Jud



