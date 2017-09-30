#=================================================================
#
#		Image Processing - GradFig
#		Copyright(c) KazukiAmakawa, all right reserved.
#
#=================================================================
#This is the main function of the program, all program will begin from this program

#import head
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
import math
import matplotlib.patches as patches

#import files
import Init

def GLLT(img):
	print("1)  Negative operation")
	print("2)  Thresholding")
	print("3)  Gray level linear transformation.")
	print("4)  Logarithmic Transformation")
	print("5)  Exponential transformation")
	InpIn = 0
	while 1:
		InpStr = input("Input the algorithm you need:")
		try:
			InpInt = int(InpStr)
		except ValueError:
			print("Input Error")
			continue
		else:
			if InpInt < 1 or InpInt > 5:
				print("Input Error")
				continue
			else:
				break
	
	if InpInt == 1:
		for i in range(0, len(img)):
			for j in range(0, len(img[i])):
				img[i][j] = 255 - img[i][j]

	if InpInt == 2:
		InpInt = 0
		while 1:
			InpStr = input("Input the Gaama you need(0 - 255, int):")
			try:
				InpInt = int(InpStr)
			except ValueError:
				print("Input Error")
				continue
			else:
				if InpInt < 0 or InpInt > 255:
					print("Input Error")
					continue
				else:
					break

		for i in range(0, len(img)):
			for j in range(0, len(img[i])):
				if img[i][j] <= InpInt:
					img[i][j] = 0
				else:
					img[i][j] = 255

	if InpInt == 3:
		InpInt1 = 0
		InpInt2 = 0
		while 1:
			InpStr = input("Now input the float C(float):  ")
			try:
				InpInt1 = float(InpStr)
			except ValueError:
				print("Input Error")
				continue
			else:
				break

		while 1:
			InpStr2 = input("Input the Gaama you need(0 - 255, int):")
			try:
				InpInt2 = int(InpStr2)
			except ValueError:
				print("Input Error")
				continue
			else:
				if InpInt2 < 0 or InpInt2 > 255:
					print("Input Error")
					continue
				else:
					break

		for i in range(0, len(img)):
			for j in range(0, len(img[i])):
				img[i][j] = InpInt1 * img[i][j] + InpInt2

	if InpInt == 4:
		InpInt1 = 0
		while 1:
			InpStr = input("Now input the float C(float):  ")
			try:
				InpInt1 = float(InpStr)
			except ValueError:
				print("Input Error")
				continue
			else:
				break
		for i in range(0, len(img)):
			for j in range(0, len(img[i])):
				img[i][j] = InpInt1 * math.log(1+img[i][j])

	if InpInt == 5:
		InpInt1 = 0
		InpInt2 = 0
		while 1:
			InpStr = input("Now input the float C:  ")
			try:
				InpInt1 = float(InpStr)
			except ValueError:
				print("Input Error")
				continue
			else:
				break

		while 1:
			InpStr2 = input("Input the b you need:")
			try:
				InpInt2 = float(InpStr2)
			except ValueError:
				print("Input Error")
				continue
			else:
				if InpInt2 < 0 or InpInt2 > 255:
					print("Input Error")
					continue
				else:
					break

		for i in range(0, len(img)):
			for j in range(0, len(img[i])):
				try:
					img[i][j] = InpInt1 * (pow(InpInt2, img[i][j]) - 1)
				except:
					print("Error !!")
					return -1
	Init.LogWrite("GLLT calculation succeed", "0")
	return img


def GPTCal(img, InpInt):
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = 255 * (pow((img[i][j] / 255), InpInt))
	Init.LogWrite("GPTCal calculation succeed", "0")
	return img


def GPT(img):
	InpInt = 0
	while 1:
		InpStr = input("Input the Gamma you need:")
		try:
			InpInt = int(InpStr)
		except ValueError:
			print("Input Error")
			continue
		else:
			break
	Init.LogWrite("GPT calculation succeed", "0")
	return img


def CST(img):
	InpInt1 = 0
	InpInt2 = 0
	ipusero = 0.01
	while 1:
		InpStr = input("Input the m you need:")
		try:
			InpInt1 = float(InpStr)
		except ValueError:
			print("Input Error")
			continue
		else:
			break

	while 1:
		InpStr = input("Input the E you need:")
		try:
			InpInt2 = float(InpStr)
		except ValueError:
			print("Input Error")
			continue
		else:
			break

	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			#print(pow((InpInt1 / img[i][j] + ipusero), InpInt2))
			img[i][j] = 255 / (1 + pow((InpInt1 / img[i][j] + ipusero), InpInt2) )
	
	Init.LogWrite("CST calculation succeed", "0")
	return img


def HE(img):
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

	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = int(255 * ProSum[int(img[i][j])])
	Init.LogWrite("MET calculation succeed", "0")
	return img



	