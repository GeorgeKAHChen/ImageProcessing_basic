#=================================================================
#
#		Image Processing - Project2.py
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

#import file
import Convolution

def MF(img):
	img1 = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			AveArr = []
			for p in range(-1, 2):
				for q in range(-1, 2):
					try:
						if i+p >= 0 and j+q >=0:
							AveArr.append(img[i][j])
						else:
							continue
					except:
						continue

			sorted(AveArr)
			img1[i][j] = AveArr[int((len(AveArr)+1)/2)]

	return img1

def SO(img):
	"""
	InpInt = 0
	while 1:
		InpStr = input("Now input the tresholding variable:  ")
		try:
			InpInt = int(InpStr)
		except:
			print("Inpur Error")
			continue
		else:
			if InpInt < 0 or InpInt > 255:
				print("Input Error")
				continue
			else:
				break
	"""
	img1 = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	img2 = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	Reimg = [[0 for n in range(len(img[0]))] for n in range(len(img))]

	kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
	img1 = Convolution.D2FFT(img,kernel)	
	kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
	img2 = Convolution.D2FFT(img,kernel)
	
	Auto = []
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			Auto.append(img1[i][j]*img1[i][j]+img2[i][j]*img2[i][j])
	sorted(Auto)

	InpInt =  math.sqrt(Auto[int(len(Auto))])
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			Auto.append(img1[i][j]*img1[i][j]+img2[i][j]*img2[i][j])
			if math.sqrt(img1[i][j]*img1[i][j]+img2[i][j]*img2[i][j]) > InpInt:
				Reimg[i][j] = 0
			else:
				Reimg[i][j] = 1

	return Reimg


def RO(img):
	img1 = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	img2 = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	Reimg = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	kernel = np.array([[0, 1], [-1, 0]])
	img1 = Convolution.NormalConvolution(img,kernel)	
	kernel = np.array([[1, 0], [0, -1]])
	img2 = Convolution.NormalConvolution(img,kernel)
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			if math.sqrt(img1[i][j]*img1[i][j]+img2[i][j]*img2[i][j]) > 30:
				Reimg[i][j] = 0
			else:
				Reimg[i][j] = 1

	return Reimg


def GOC(img):
	img1 = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	img2 = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	Reimg = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	kernel = np.array([[-1, 1]])
	img1 = Convolution.NormalConvolution(img,kernel)	
	kernel = np.array([[1, -1]])
	img2 = Convolution.NormalConvolution(img,kernel)
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			if math.sqrt(img1[i][j]*img1[i][j]+img2[i][j]*img2[i][j]) > 30:
				Reimg[i][j] = 0
			else:
				Reimg[i][j] = 1

	return Reimg


def SVSF(img):
	InpInt = 0
	while 1:
		InpStr = input("Now input the size of kernel:  ")
		try:
			InpInt = int(InpStr)
		except:
			print("Input Error")
			continue
		else:
			if InpInt <= 1:
				print("Input Error")
				continue
			elif InpInt % 2 != 1:
				print("Must confident the size of kernel as a Odd number.")
				continue
			else:
				break 
	Len = int((InpInt-1)/2 + 0.5)
	Left = -Len
	Right = Len + 1
	img1 = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	for i in range(0, len(img)):
		for j in range(0, len(img[0])):
			TTL = 0.00
			for p in range(Left, Right):
				for q in range(Left, Right):
					try:
						TTL += img[i+p][j+q]
					except:
						continue
			TTL /= 9
			Var = 0
			for p in range(Left, Right):
				for q in range(Left, Right):
					try:
						Var += pow((img[i+p][j+q] - TTL), 2)
					except:
						continue
			Var /= 9
			img1[i][j] = int(Var)
	return img1

