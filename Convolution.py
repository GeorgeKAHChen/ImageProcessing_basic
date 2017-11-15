#=================================================================
#
#		Image Processing - Convolution
#		Copyright(c) KazukiAmakawa, all right reserved.
#
#=================================================================
#Just For Convolution
#import head
 

#import files
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
import math
import matplotlib.patches as patches
from scipy import misc
from scipy import signal
from collections import deque
import time

#import files
import Init
import os

def D2FFT(InpX, InpK):
	return signal.fftconvolve(InpX, InpK[::-1], mode='full')
	"""
	LenX = len(InpX[0])
	LenY = len(InpX)
	ArrK = np.array([[0.00 for n in range(LenX)] for m in range(LenY)])
	C = [[0 for n in range(LenX)] for n in range(LenY)]
	for i in range(0, len(InpK)):
		for j in range(0, len(InpK[i])):
			ArrK[i][j] = InpK[i][j]
	
	LenX = pow(2, int( math.log2( len(InpX[0]) + len(InpK[0]) ) ) + 1)
	LenY = pow(2, int( math.log2( len(InpX) + len(InpK) ) ) + 1)

	ArrX = np.array([[0.00 for n in range(LenX)] for m in range(LenY)])
	
	
	for i in range(0, len(InpX)):
		for j in range(0, len(InpX[i])):
			ArrX[i][j] = InpX[i][j]

	
	ArrX = InpX
	FFTX = np.fft.fft2(ArrX)
	Init.ArrOutput(FFTX)
	FFTK = np.fft.fft2(ArrK)
	time.sleep(10)
	Init.ArrOutput(FFTK)
	FFTXK = FFTX * FFTK
	B = np.fft.ifft2(FFTXK).real
	for i in range(0, len(B)):
		for j in range(0, len(B[i])):
			B[i][j] = min(255, B[i][j])
			B[i][j] = max(0, B[i][j])
			C[i][j] = int(B[i][j])
	Init.ArrOutput(C)
	return C
	"""


def NormalConvolution(img, kernel):
	CenX = 0
	CenY = 0
	NegX = 0
	NegY = 0
	PosX = 0
	PosY = 0
	img1 = [[0 for n in range(len(img[0]))]for n in range(len(img))]

	if len(kernel) % 2 == 1 and len(kernel[0]) % 2 == 1:
		CenX = int((len(kernel)-1)/2+0.5)
		CenY = int((len(kernel[0])-1)/2+0.5)
	else:
		for i in range(0, len(kernel)):
			for j in range(0, len(kernel[i])):
				print(kernel[i][j], end = "\t")
			print()
		print()
		while 1:
			InpStr = input("Now input the row of array:  ")
			try:
				CenX = int(InpStr)
			except:
				print("Input Error")
				continue
			else:
				if CenX < 0 or CenX >= len(kernel):
					print("Input Error")
					continue	
				else:
					break

		while 1:
			InpStr = input("Now input the column of array:  ")
			try:
				CenY = int(InpStr)
			except:
				print("Input Error")
				continue
			else:
				if CenY < 0 or CenY >= len(kernel):
					print("Input Error")
					continue	
				else:
					break								

	NegX = -CenX
	NegY = -CenY
	PosX = len(kernel) - CenX
	PosY = len(kernel[0]) - CenY
	Ima = -1
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			
			if Ima != int((i*len(img) + j)/( (len(img)-1)*(len(img[1])-1) ) * 100/0.83):
				if Ima <= 100:
					Ima = int((i*len(img) + j)/( (len(img)-2)*(len(img[1])-2) ) * 100/0.83)
					print("Convolution: " + str(Ima) + "%", end = "\r")

			#print([i, j])
			for p in range(NegX, PosX):
				for q in range(NegY, PosY):
					Tem = 0
					try:
						if i+p >= 0 and j+q >= 0:
							Tem = img[i+p][j+q]
					except:
						Tem = 0

					img1[i][j] += Tem * kernel[CenX+p][CenY+q]
			#print(img1[i][j])
			img1[i][j] = min(255, int(img1[i][j]))
			img1[i][j] = max(0, int(img1[i][j]))
	if Ima <= 100:
		print("Convolution: 100%")
	return img1


def Convolution(img):
	os.system('clear')
	Kernel = None
	InpStr = ""
	InpInt = 0
	print("1)  [[1, 1, 1], [1, 1, 1], [1, 1, 1]] / 9")
	print("2)  [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]] / 25")
	print()
	print("3)  [[1, 1, 1], [1, 2, 1], [1, 1, 1]] / 10")
	print("4)  [[1, 2, 1], [2, 4, 2], [1, 2, 1]] / 16")
	print("5)  [[1, 1, 1], [1, 0, 1], [1, 1, 1]] / 9")
	print()
	print("6)  [[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4],[1, 4, 7, 4, 1]] / 273")
	print()
	print("7)  [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]")
	print("8)  [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]")
	print()
	print("9)  [[1 * 129] * 129]]")
	print()
	print("10) [[1], [-1]]")
	print("11) [[1, -1]]")
	print("12) [[0, 1], [-1, 0]]")
	print("13) [[1, 0], [0, -1]]")
	print()
	print("14) [[1, 1, 1,], [0, 0, 0], [-1, -1, -1]]")
	print("15) [[1, 0, -1], [1, 0, -1], [1, 0, -1]]")
	print()
	print("16) [[0, 1, 0], [1, -4, 1], [0, 1, 0]]")
	print("17) [[1, 1, 1], [1, -8, 1], [1, 1, 1]]")
	print("18) [[0, 0, 1, 0, 0], [0, 1, 2, 1, 0], [1, 2, -16, 2, 1], [0, 1, 2, 1, 0], [0, 0, 1, 0 ,0]]")
	print("19) [[2, 4, 5, 4, 2], [4, 9, 12, 9, 4], [5, 12, 15, 12, 5], [4, 9, 12, 9, 4], [2, 4, 5, 4, 2]]")
	print()
	print("20) High-boost [0, -1, 0], [-1, 8, -1], [0, -1, 0]")
	print("21) High-boost [-1, -1, -1], [-1, 16, -1], [-1, -1, -1]")
	print("0)  EXIT")
	while 1:
		InpStr = input("Input the kernal number you need:  ")
		try:
			InpInt = int(InpStr)
		except:
			print("Input Error")
			continue
		else:
			if InpInt < 0 or InpInt > 30:
				print("Input Error")
				continue
			else:
				break
	if InpInt == 0:
		return img
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
	if InpInt == 9:
		Kernel = np.array([[1 for n in range(129)] for n in range(129)])/129
	if InpInt == 10:
		Kernel = np.array([[1], [-1]])
	if InpInt == 11:
		Kernel = np.array([[1, -1]])
	if InpInt == 12:
		Kernel = np.array([[0, 1], [-1, 0]])		
	if InpInt == 13:
		Kernel = np.array([[1, 0], [0, -1]])
	if InpInt == 14:
		Kernel = np.array([[1, 1, 1,], [0, 0, 0], [-1, -1, -1]])
	if InpInt == 15:
		Kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
	if InpInt == 16: 
		Kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
	if InpInt == 17:
		Kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
	if InpInt == 18:
		Kernel = np.array([[0, 0, 1, 0, 0], [0, 1, 2, 1, 0], [1, 2, -16, 2, 1], [0, 1, 2, 1, 0], [0, 0, 1, 0 ,0]])
	if InpInt == 19:
		Kernel = np.array([[2, 4, 5, 4, 2], [4, 9, 12, 9, 4], [5, 12, 15, 12, 5], [4, 9, 12, 9, 4], [2, 4, 5, 4, 2]]) / 115
	if InpInt == 20:
		Kernel = np.array([[0, -1, 0], [-1, 8, -1], [0, -1, 0]])
	if InpInt == 21:
		Kernel = np.array([[-1, -1, -1], [-1, 16, -1], [-1, -1, -1]])
		#Kernel = np.array([[]])
		#Kernel = np.array([[]])
	"""
	InpInt = 0
	print("1)  Normal Convolution method")
	print("2)  FFT-IFFT Method")

	while 1:
		InpStr = input("Now input the way to convolution:  ")
		try:
			InpInt = int(InpStr)
		except:
			print("Input Error")
			continue
		else:
			if InpInt < 0 or InpInt > 2:
				print("Input Error")
				continue	
			else:
				break

	if InpInt == 1:
		img = NormalConvolution(img, Kernel)
	else:
		NewImg = D2FFT(img, Kernel)
		for i in range(0, len(img)):
			for j in range(0, len(img[0])):
				try:
					img[i][j] = NewImg[i+1][j+1] 
				except:
					print("Error")
					return [0]
	"""
	NewImg = D2FFT(img, Kernel)
	for i in range(0, len(img)):
		for j in range(0, len(img[0])):
			try:
				img[i][j] = NewImg[i+1][j+1] 
			except:
				print("Error")
				return [0]
	Init.ArrOutput(img)
	return img











