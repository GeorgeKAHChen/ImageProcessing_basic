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


#import files
import GradFig
import Init
import Proj1
import MTRand
import TimeCal


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

				

