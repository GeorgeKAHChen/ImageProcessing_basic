#=================================================================
#
#		Image Processing - Convolution
#		Copyright(c) KazukiAmakawa, all right reserved.
#
#=================================================================
#Just For Convolution
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

#import files


def D2FFT(InpX, InpK):
	LenX = pow(2, int( math.log2( len(InpX[0]) + len(InpK[0]) ) ) + 1)
	LenY = pow(2, int( math.log2( len(InpX) + len(InpK) ) ) + 1)

	ArrX = np.array([[0.00 for n in range(LenX)] for m in range(LenY)])
	ArrK = np.array([[0.00 for n in range(LenX)] for m in range(LenY)])
	
	for i in range(0, len(InpX)):
		for j in range(0, len(InpX[i])):
			ArrX[i][j] = InpX[i][j]

	for i in range(0, len(InpK)):
		for j in range(0, len(InpK[i])):
			ArrK[i][j] = InpK[i][j]

	print(ArrX)
	print(ArrK)
	FFTX = np.fft.fft2(ArrX)
	FFTK = np.fft.fft2(ArrK)
	FFTXK = FFTX * FFTK
	B = np.fft.ifft2(FFTXK).real
	return B


def Convolution(img):
	os.system('clear')
	Kernel = None
	InpStr = ""
	InpInt = 0
	print("1)  [[1, 1, 1], [1, 1, 1], [1, 1, 1]] / 9")
	print("2)  [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]] / 25")
	print("3)  [[1, 1, 1], [1, 2, 1], [1, 1, 1]] / 10")
	print("4)  [[1, 2, 1], [2, 4, 2], [1, 2, 1]] / 16")
	print("5)  [[1, 1, 1], [1, 0, 1], [1, 1, 1]] / 9")
	print("6)  [[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4],[1, 4, 7, 4, 1]] / 273")
	print("7)  [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]")
	print("8)  [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]")
	print("9)  ")
	print("10) ")
	print("0)  EXIT")
	while 1:
		InpStr = input("Input the kernal number you need.")
		try:
			InpInt = int(InpStr)
		except:
			print("Input Error")
			continue
		else:
			if InpInt < 1 or InpInt > 8:
				print("Input Error")
				continue
			else:
				break
	if InpInt == 0:
		return 
	if InpInt == 1:
		Kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9
	if InpInt == 2:
		Kernel = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) / 25
	if InpInt == 3:
		Kernal = np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]]) / 10
	if InpInt == 4:
		Kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
	if InpInt == 5:
		Kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) / 9
	if InpInt == 6:
		Kernel = np.array([[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4],[1, 4, 7, 4, 1]]) / 273
	if InpInt == 7:
		Kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
	if InpInt == 8:
		Kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
		#Kernel = np.array([])
	NewImg = D2FFT(img, Kernel)
	for i in range(0, len(img)):
		for j in range(0, len(img[0])):
			try:
				img[i][j] = NewImg[i+1][j+1] 
			except:
				img[i][j] = img[i][j]
	return img











