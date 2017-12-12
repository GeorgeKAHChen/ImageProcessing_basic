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


def PrintFig(ay, maxx):
	#Establish the figure
	fig1 = plt.figure()
	ax = fig1.add_subplot(111)
	
	#x y lim setting	
	plt.xlim(-1, 270)
	plt.ylim(0, maxx)

	#Printing loop
	for i in range(0, len(ay)):
		ax.add_patch(patches.Rectangle((i, 0), 1, ay[i], color = 'black'))

	#Saving and output
	fig1.show()
	
	input('Press Enter key to continue')
	return


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


def HFT(img):
	His = [0 for n in range(260)]
	
	"""
	His[0] = 10000
	#His[63] = 10000
	His[127] = 10000
	#His[191] = 10000
	His[255] = 10000

	"""
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			His[img[i][j]] += 1
	

	sb = 0
	for i in range(0, len(His)):
		sb = max(sb, His[i])
	

	PrintFig(His, sb * 1.5)

	HF = [0 for n in range(260)]
	
	HF = np.fft.fft(His).real
	#HF = np.fft.fftshift(HF)
	HF = np.abs(HF)
	sb = 0
	for i in range(0, len(His)):
		sb = max(sb, His[i])
	"""
	for i in range(0, 257):
		HF[i] = His[i+1] - His[i]
	"""
	PrintFig(HF, sb*4)

	#理论可行，接下来考虑怎么取一个周期
	#通过一个周期内的极值判定解决问题






