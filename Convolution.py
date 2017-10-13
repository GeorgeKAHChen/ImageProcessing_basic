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

	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
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
	
	return img1


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
	print("9)  [[1 * 129] * 129]]")
	print("10) [[1], [-1]]")
	print("11) [[1, -1]]")
	print("12) [[0, 1], [-1, 0]]")
	print("13) [[1, 0], [0, -1]]")
	print("14) [[1, 1, 1,], [0, 0, 0], [-1, -1, -1]]")
	print("15) [[1, 0, -1], [1, 0, -1], [1, 0, -1]]")
	print("0)  EXIT")
	while 1:
		InpStr = input("Input the kernal number you need:  ")
		try:
			InpInt = int(InpStr)
		except:
			print("Input Error")
			continue
		else:
			if InpInt < 0 or InpInt > 20:
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
		Kernel = np.array([[1 for n in range(15)] for n in range(15)])/15
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
		#Kernel = np.array([[]])
		#Kernel = np.array([[]])
		#Kernel = np.array([[]])
		#Kernel = np.array([[]])
	
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
	print("Baka!")
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			print(img[i][j], end = "\t")
		print()


	return img











