#=================================================================
#
#		Image Processing - Transfromation
#		Copyright(c) KazukiAmakawa, all right reserved.
#
#=================================================================
"""
This file will include some transformation method
FT: Fourier Transform
LT: Laplacian Transform
ZT: Z-transfrom
WT: Wavelet Transform
"""

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

#import files
import Init


def FT(img):
	PFT = np.fft.fft2(img)
	TSF = np.fft.fftshift(PFT)
	FT = np.abs(TSF)
	#Init.ArrOutput(FT)
	Maxx = -9999999999
	for i in range(0, len(FT)):
		for j in range(0, len(FT[i])):
			Maxx = max(Maxx, FT[i][j])
	for i in range(0, len(FT)):
		for j in range(0, len(FT[i])):
			FT[i][j] = int(FT[i][j] / Maxx * 255)
			FT[i][j] = max(0, FT[i][j])
			FT[i][j] = min(255, FT[i][j])


	#Init.ArrOutput(FT)
	return FT


def LP(img):
	return


def ZP(img):
	return


def WP(img):
	return










