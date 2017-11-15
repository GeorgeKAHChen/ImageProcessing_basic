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
from collections import deque

#import files
import Init


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
	Init.LogWrite("MET calculation succeed", "0")
	return img


def NO(img):
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = 255 - img[i][j]
	return img


def TS(img, InpInt):
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			if img[i][j] <= InpInt:
				img[i][j] = 0
			else:
				img[i][j] = 255
	return img


def GLL(img, InpInt1, InpInt2):
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = min(InpInt1 * img[i][j] + InpInt2, 255)

	return img


def LT(img, InpInt1):
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = min(InpInt1 * math.log(1+img[i][j]), 255)

	return img


def ET(img, InpInt1, InpInt2):
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			try:
				img[i][j] = min(InpInt1 * (pow(InpInt2, img[i][j]) - 1), 255)
			except:
				print("Error !!")
				return -1
	return img


def LTM(img, InpInt1):
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = min(InpInt1 * img[i][j], 255)
	return img


def GLLT(img):
	print("1)  Negative operation")
	print("2)  Thresholding")
	print("3)  Gray level linear transformation.")
	print("4)  Logarithmic Transformation")
	print("5)  Exponential transformation")
	print("6)  Linear Treatment")
	InpIn = 0
	while 1:
		InpStr = input("Input the algorithm you need:")
		try:
			InpInt = int(InpStr)
		except ValueError:
			print("Input Error")
			continue
		else:
			if InpInt < 1 or InpInt > 6:
				print("Input Error")
				continue
			else:
				break
	
	if InpInt == 1:
		img = NO(img)

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
		img = TS(img, InpInt)

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
		img = GLL(img, InpInt1, InpInt2)

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
		img = LT(img, InpInt1)

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
		img = ET(img, InpInt1, InpInt2)

	if InpInt == 6:
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
		img = LTM(img, InpInt1)

	Init.LogWrite("GLLT calculation succeed", "0")
	return img


def GPTCal(img, InpInt):
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = min(255 * (pow((img[i][j] / 255), InpInt)), 255)
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
			img[i][j] = min(255 / (1 + pow((InpInt1 / img[i][j] + ipusero), InpInt2) ), 255)
	
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
			img[i][j] = min(int(255 * ProSum[int(img[i][j])]), 255)
	Init.LogWrite("MET calculation succeed", "0")
	return img


