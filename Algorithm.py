#=================================================================
#
#		Image Processing - Algorithm
#		Copyright(c) KazukiAmakawa, all right reserved.
#
#=================================================================
#This program will use algorithm directly. And the variable will automaticlly choose.
#It is important to make the program fast and easier

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
import random
import cv2

#import files
import GradFig
import Init
import Proj1
import MTRand
import TimeCal
import Convolution


def Algorithm(img):
	SavingArr = deque()
	NumArr = deque()
	SavingArr.append([1.000, 100.000])
	Usingimg = img.copy()
	Var1 = GradFig.FigSta(Proj1.LT(Usingimg, 1.000), 1)[2]
	Usingimg = img.copy()
	Var2 = GradFig.FigSta(Proj1.LT(Usingimg, 100.000), 1)[2]
	NumArr.append([Var1, Var2])
	Output = 0
	item = 0

	while 1:
		print(SavingArr)
		print(NumArr)
		NowArr = SavingArr.pop()
		NowNum = NumArr.pop()
		if NowNum[1] - NowNum[0] < 0.1 or NowArr[1] - NowArr[0] < 0.0001:
			Output = (NowArr[0] + NowArr[1]) / 2
			break

		Ave = (NowArr[0] + NowArr[1]) / 2
		Usingimg = img.copy()
		
		Num = GradFig.FigSta(Proj1.LT(Usingimg, Ave), 1)[2]
		
		if (NowNum[0] - 128) * (Num - 128) < 0:
			SavingArr.append([NowArr[0], Ave])
			NumArr.append([NowNum[0], Num])
		elif (NowNum[0] - 128) * (Num - 128) == 0:
			Output = (NowArr[0] + Ave)/2
			break

		if (NowNum[1] - 128) * (Num - 128) < 0:
			SavingArr.append([Ave, NowArr[1]])
			NumArr.append([Num, NowNum[1]])
		elif (NowNum[1] - 128) * (Num - 128) == 0:
			Output = (Ave + NowArr[1]) / 2 
			break

	print(Output)

	return Proj1.LT(img, Output)


def Algorithm01(img):
	SavingArr = deque()
	NumArr = deque()
	SavingArr.append([0.001, 100.00])
	Usingimg = img.copy()
	Var1 = GradFig.FigSta(Proj1.LTM(Usingimg, 0.001), 1)[0]
	Usingimg = img.copy()
	Var2 = GradFig.FigSta(Proj1.LTM(Usingimg, 100.00), 1)[0]
	NumArr.append([Var1, Var2])
	Output = 0
	item = 0

	while 1:
		print(SavingArr)
		print(NumArr)
		NowArr = SavingArr.pop()
		NowNum = NumArr.pop()
		if NowNum[1] - NowNum[0] < 0.1 or NowArr[1] - NowArr[0] < 0.0001:
			Output = (NowArr[0] + NowArr[1]) / 2
			break

		Ave = (NowArr[0] + NowArr[1]) / 2
		Usingimg = img.copy()
		
		Num = GradFig.FigSta(Proj1.LTM(Usingimg, Ave), 1)[0]
		
		if (NowNum[0] - 128) * (Num - 128) < 0:
			SavingArr.append([NowArr[0], Ave])
			NumArr.append([NowNum[0], Num])
		elif (NowNum[0] - 128) * (Num - 128) == 0:
			Output = (NowArr[0] + Ave)/2
			break

		if (NowNum[1] - 128) * (Num - 128) < 0:
			SavingArr.append([Ave, NowArr[1]])
			NumArr.append([Num, NowNum[1]])
		elif (NowNum[1] - 128) * (Num - 128) == 0:
			Output = (Ave + NowArr[1]) / 2 
			break

	print(Output)

	return Proj1.LTM(img, Output)


def MCAC(img):
	#Monte Carlo Average Constrast
	#Design by Kazuki Amakawa
	Xleng = len(img)
	Xmax = 0
	Yleng = len(img[0])
	Ymax = 0
	Group = 0
	while 1:
		if Xleng == 0:
			break
		else:
			Xleng = int(Xleng / 10)
			Xmax += 1
	while 1:
		if Yleng == 0:
			break
		else:
			Yleng = int(Yleng / 10)
			Ymax += 1

	XSize = len(img)
	YSize = len(img[0])
	RanStr = str(MTRand.MT19937(TimeCal.GetTime()).extract_number())
	while 1:
		for kase in range(0, 1000):
			XNum = 0
			YNum = 0
			while 1:
				Str = ""
				while 1:
					RanStr = str(MTRand.MT19937(int(RanStr)).extract_number())		
					TemStr = ""
					for i in range(len(RanStr), 10):
						TemStr += "0"
					for i in range(0, len(RanStr)):
						TemStr += RanStr

					for i in range(0, len(TemStr)-1):
						Str += TemStr[i]
					if len(Str) < Xmax:
						continue
					else:
						break

				XStr = ""
				for i in range(0, Xmax):
					XStr += Str[i]
				XNum = int(XStr)
				if XNum <= XSize:
					break
				else:
					continue

			
			while 1:
				Str = ""
				while 1:
					RanStr = str(MTRand.MT19937(int(RanStr)).extract_number())			
					TemStr = ""
					for i in range(len(RanStr), 10):
						TemStr += "0"
					for i in range(0, len(RanStr)):
						TemStr += RanStr

					for i in range(0, len(TemStr)-1):
						Str += TemStr[i]
					if len(Str) < Ymax:
						continue
					else:
						break

				YStr = ""
				for i in range(0, Ymax):
					YStr += Str[i]
				YNum = int(YStr)
				if YNum <= YSize:
					break
				else:
					continue

			Arr = []
			for i in range(XNum-5, XNum+5):
				for j in range(YNum-5, YNum+5):
					try:
						Arr.append(img[i][j])
					except:
						continue

			Arr = sorted(Arr)
			Tem = int(len(Arr) / 2) + 1
			Add = Arr[Tem] - 128
			for i in range(XNum-5, XNum+5):
				for j in range(YNum-5, YNum+5):
					try:
						img[i][j] += Add
					except:
						continue
		Output = GradFig.FigSta(img, 1)[2]
		Group += 1

		return img
		if Output == 128:
			break
		else:
			continue
	return img


def MCHE(img):
	Xleng = len(img)
	Xmax = 1
	Yleng = len(img[0])
	Ymax = 1
	Group = 0
	while 1:
		if Xleng == 0:
			break
		else:
			Xleng = int(Xleng / 10)
			Xmax += 1
	while 1:
		if Yleng == 0:
			break
		else:
			Yleng = int(Yleng / 10)
			Ymax += 1

	XSize = len(img)
	YSize = len(img[0])
	RanStr = str(MTRand.MT19937(TimeCal.GetTime()).extract_number())
	while 1:
		for kase in range(0, 100):
			XNum = 0
			YNum = 0
			while 1:
				Str = ""
				while 1:
					RanStr = str(MTRand.MT19937(int(RanStr)).extract_number())		
					TemStr = ""
					for i in range(len(RanStr), 10):
						TemStr += "0"
					for i in range(0, len(RanStr)):
						TemStr += RanStr

					for i in range(0, len(TemStr)-1):
						Str += TemStr[i]
					if len(Str) < Xmax:
						continue
					else:
						break

				XStr = ""
				for i in range(0, Xmax):
					XStr += Str[i]
				XNum = int(XStr)
				if XNum <= XSize:
					break
				else:
					continue

			
			while 1:
				Str = ""
				while 1:
					RanStr = str(MTRand.MT19937(int(RanStr)).extract_number())			
					TemStr = ""
					for i in range(len(RanStr), 10):
						TemStr += "0"
					for i in range(0, len(RanStr)):
						TemStr += RanStr

					for i in range(0, len(TemStr)-1):
						Str += TemStr[i]
					if len(Str) < Ymax:
						continue
					else:
						break

				YStr = ""
				for i in range(0, Ymax):
					YStr += Str[i]
				YNum = int(YStr)
				if YNum <= YSize:
					break
				else:
					continue

			img2 = [[0.00 for n in range(25)] for n in range(25)]
			for i in range(XNum - 12, XNum + 13):
				for j in range(YNum - 12, YNum + 13):
					try:
						img2[i - XNum + 12][j - YNum + 12] = img[i][j]
					except:
						img2[i - XNum + 12][j - YNum + 12] = 0

			img2 = Proj1.HE(img2)
			
			for i in range(0, 25):
				for j in range(0, 25):
					try:
						img[i + XNum - 12][j + YNum - 12] = img2[i][j]
					except:
						continue

		Tem = GradFig.FigSta(img, 2)[2]
		print(Tem)
		
		if Tem == 128:
			break
	return img


def CED(img):
	#Canny edge detector
	#With opencv method
	return cv2.Canny(img,100,100)
	
	#Normal Code
	#Step 1
	"""
	Kernel = np.array([[2, 4, 5, 4, 2], [4, 9, 12, 9, 4], [5, 12, 15, 12, 5], [4, 9, 12, 9, 4], [2, 4, 5, 4, 2]]) / 115
	img = Convolution.D2FFT(img, Kernel)
	
	img1 = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	img2 = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	Dir = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	Reimg = [[0 for n in range(len(img[0]))] for n in range(len(img))]

	#Step 2
	PI = 3.1415926535897932384626
	kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
	img1 = Convolution.D2FFT(img,kernel)	
	kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
	img2 = Convolution.D2FFT(img,kernel)
	Treasholding = 50

	#Step 3
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			Ang = math.atan(img1[i][j]/img2[i][j])
			if Ang <= PI/8 or (Ang > 7*PI/8 and Ang < 9*PI/8) or Ang > 15*PI/8:
				Dir[i][j] = 0
			if (Ang > PI/8 and Ang <= 3*PI/8) or (Ang > 9*PI/8 and Ang <= 11*PI/8):
				Dir[i][j] = PI/4
			if (Ang > 3*PI/8 and Ang <= 5*PI/8) or (Ang > 11*PI/8 and Ang <= 13*PI/8):
				Dir[i][j] = PI/2
			else:
				Dir[i][j] = 3*PI/4
				
			Dir[i][j] = 
			if math.sqrt(img1[i][j]*img1[i][j]+img2[i][j]*img2[i][j]) > Treasholding:
				img[i][j] = 0
			else:
				img[i][j] = 1



	return img
	"""

"""
def MF(img):
	for leng in range(1, 50)
		for i in range(0, len(img)):
			for j in range(0, len(img[i])):
				SortImg = []
				head = 0
				for p in range(-leng, leng+1):
					for q in range(-leng, leng+1):
						try:
							Saving = [img[i+p][j+p], p, q, 0]
						except:
							continue

						if len(SortImg) == 0:
							SortImg.append(Saving)
							continue
						walk = head
						while 1:
							if head == -1:
								break
							else:
								pass


def SNMF(img):
	#Symmetric neighbor smoothing filter.
	Reimg = [[0 for n in range(len(img[1]))] for n in range(len(img))]
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			AnoImg = []
			Error = False
			for p in range(-1, 2):
				for q in range(-1, 2):
					try:
						AnoImg.append(img[i+p][j+q])
					except:	
						Error =True
				if Error == True:
					brewk
			if Error == True:
				continue

			else:
				

"""

def RWPI(img):
	alpha = 5.00
	beta = 1.00
	e = 2.71828182846
	Reimg = [[0 for n in range(len(img[1]))] for n in range(len(img))]
	Point = [[0, 0] for n in range(10)]
	for i in range(0, len(Point)):
		Point[i][0] = random.randint(5, len(img)-5)
		Point[i][1] = random.randint(5, len(img[1])-5)
	Kase = 0
	Pre = 0

	while 1:
		if Kase == len(img) * len(img[i]):
			break
		else:
			Kase += 1

		if Pre != int(100 * Kase / (len(img) * len(img[i]))):
			Pre += 1
			print(str(Pre) + "%")

		for m in range(0, len(Point)):
			i = Point[m][0]
			j = Point[m][1]
			#print([i, j])
			Reimg[i][j] += 1
			NewLoc = []
			for p in range(-1, 2):
				for q in range(-1, 2):
					Step = [0.00, 0, p, q]
					if p == 0 and q == 0:
						continue
					else:
						try:
							Step[1] = abs(img[i][j] - img[i+p][j+q])
						except:
							continue
					Step[0] = pow(e, (-((abs(p)+abs(q))/alpha) - (Step[1]/beta)))
					NewLoc.append(Step)
			TTL = 0.00
			for i in range(0, len(NewLoc)):
				TTL += NewLoc[i][0]
			Maxx = int(TTL)
			Num = random.randint(0, Maxx)
			TTL2 = 0
			Final = 0
			for i in range(0, len(NewLoc)):
				TTL2 += NewLoc[i][0]
				if TTL2 >= Num:
					Final = i
					break
			Point[m][0] += NewLoc[Final][2]
			Point[m][1] += NewLoc[Final][3]

	for i in range(0, len(Reimg)):
		for j in range(0, len(Reimg[i])):
			if Reimg[i][j] != 0:
				Reimg[i][j] = 255
	return Reimg

	mini = 99999999
	maxi = 0
	for i in range(0, len(Reimg)):
		for j in range(0, len(Reimg[i])):
			mini = min(Reimg[i][j], mini)
			maxi = max(Reimg[i][j], maxi)

	for i in range(0, len(Reimg)):
		for j in range(0, len(Reimg[i])):
			Reimg[i][j] = int((Reimg[i][j] - mini)/(maxi-mini) * 255)

	return Reimg













