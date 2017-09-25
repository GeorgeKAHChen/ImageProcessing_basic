from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
import math

def FigureInput():
	Figure = []
	for root, dirs, files in os.walk(os.getcwd()):
		FilesArr = files

	Figure = []
	for i in range(0, len(FilesArr)):
		Hajimari = 0
		Last = ""
		for j in range(0, len(FilesArr[i])):
			if FilesArr[i][j] == ".":
				Hajimari = 1
				continue
			elif FilesArr[i][j] == "\n":
				Hajimari = 0
				continue
			elif Hajimari == 1:
				Last += str(FilesArr[i][j])
			else:
				continue

		if Last == "bmp" or Last == "jpg" or Last == "png":
			Figure.append(FilesArr[i])

	for i in range(0, len(Figure)):
		print(str(i+1) + "\t" + Figure[i])

	InpInt = 0
	while 1:
		InpStr = input("Choose a figure with code:  ")
		try:
			InpInt = int(InpStr)
		except ValueError:
			print("Input Error")
			continue
		else:
			if InpInt < 1 or InpInt > len(Figure):
				print("input Error")
				continue
			else:
				break

	NameStr = Figure[InpInt-1]
	return np.array(Image.open(NameStr).convert("L"))


def Output(img):
	plt.imshow(img, cmap="gray")
	plt.axis("off")
	plt.show()
	input("Press Enter to continue")


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
				img[i][j] = InpInt1 * (pow(InpInt2, img[i][j]) - 1)
	return img


def GPTCal(img, InpInt):
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = 255 * (pow((img[i][j] / 255), InpInt))

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
	
	return img


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
	Output(img)


def MainFunction():
	img = FigureInput()
	print("1)  Gray level linear transformation.")
	print("2)  Gamma(power) transformation.")
	print("3)  Contrast-Stretching Transformations.")
	print("4)  Histogram Equalization")
	print("5)  Maximum entropy for thresholding")
	print("0)　EXIT")
	InpInt = 0
	while 1:
		InpStr = input("Input the algorithm you need:")
		try:
			InpInt = int(InpStr)
		except ValueError:
			print("Input Error")
			continue
		else:
			if InpInt < 0 or InpInt > 5:
				print("Input Error")
				continue
			else:
				break

	if InpInt == 0:
		return 
	if InpInt == 1:
		img = GLLT(img)
	if InpInt == 2:
		img = GPT(img)
	if InpInt == 3:
		img = CST(img)
	if InpInt == 4:
		img = HE(img)
	if InpInt == 5:
		img = MET(img)
		MainFunction()
		return

	Output(img)
	MainFunction()
	return


MainFunction()






