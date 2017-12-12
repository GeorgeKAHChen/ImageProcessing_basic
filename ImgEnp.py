#=================================================================
#
#		Image Processing - ImgEnp.py
#		Copyright(c) KazukiAmakawa, all right reserved.
#
#=================================================================
#import head
from copy import deepcopy
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path
import math
import matplotlib.patches as patches
from collections import deque
import random 
import cv2
import random 

#import files
import Init
import Convolution


def GetEnp(img):
	Pixel = [0 for n in range(260)]
	Prob = [0.00 for n in range(260)]
	TTL = 0
	for i in range(0, len(img)):
		for j in range(0, len(img)):
			Pixel[img[i][j]] += 1
			TTL += 1

	for i in range(0, len(Prob)):
		Prob[i] = Pixel[i] / TTL

	Entropy = 0.00
	for i in range(0, len(Prob)):
		if Prob[i] == 0:
			continue
		else:
			Entropy -= Prob[i] * math.log(Prob[i], 2)
	return Entropy


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
				img[i][j] = 255
			else:
				img[i][j] = 0

	return img


def Toboggan(img):
	SavArr = [[-1 for n in range(len(img[0]))] for n in range(len(img))]
	Gradient = [[0 for n in range(len(img[0]))] for n in range(len(img))]

	#Get Gradient
	img1 = cv2.Sobel(img, cv2.CV_16S, 1, 0)
	img2 = cv2.Sobel(img, cv2.CV_16S, 0, 1)

	for i in range(0, len(img1)):
		for j in range(0, len(img1[i])):
			Gradient[i][j] = int(math.sqrt(pow(img1[i][j], 2)+pow(img2[i][j], 2)))

	Tem = 0
	Tem1 = -1
	Color = [[0, 0]]
	Loc = [[0, 0]]
	#MainLoop
	for i in range(1, len(SavArr)-1):
		for j in range(1, len(SavArr[i])-1):
			if SavArr[i][j] != -1:
				continue

			Stack = [[i, j]]
			Tem += 1
			Color.append([0, 0])
			Loc.append([0, 0])
			while 1:
				if len(Stack) == 0:
					break

				Block = []
				Vari = Stack[len(Stack)-1][0]
				Varj = Stack[len(Stack)-1][1]
				Stack.pop()
				if SavArr[Vari][Varj] == -1:
					SavArr[Vari][Varj] = Tem
					Color[len(Color)-1][0] += 1
					Color[len(Color)-1][1] += img[Vari][Varj]
					Loc[len(Color)-1][0] += Vari
					Loc[len(Color)-1][1] += Varj
				else:
					continue
			
				if Tem != Tem1:
					print("Block:\t" + str(Tem), end = "\r")
					Tem1 = Tem

				for p in range(-1, 2):
					for q in range(-1, 2):
						Poi = 0
						try:
							Poi = Gradient[Vari+p][Varj+q]
						except:
							continue
						Block.append([Gradient[Vari+p][Varj+q], Vari+p, Varj+q])

				Block.sort()
				for k in range(0, len(Block)):
					if SavArr[Block[k][1]][Block[k][2]] == -1 and Block[k][1] > 0 and Block[k][2] > 0:
						#This judgement may have some bug
						Stack.append([Block[k][1], Block[k][2]])
						break
					
	print("Block:\t" + str(Tem), end = "\n")

	return SavArr


def GetBoundary(Tobimg):
	"""
	BFS(LocX, LocY, Node)
		This function is used for breath first search algorithm.
		The main idea of this function is traversal all the figure to find the boundary of figure

		LocX = The x Location will judge
		LocY = The y Location will judge
		Node = The Block Code of all the figure, if the node is changed, that means this block is boundary 

		return 1: means the block code had been changed
			   0: means the block has not been changed
	Also, this function will use the functional array ReFig
	"""

	ReFig = [[-1 for n in range(len(Tobimg[0]))] for n in range(len(Tobimg))]
	
	def BFS(LocX, LocY, Node):
		if LocX >= len(ReFig) or LocY >= len(ReFig[0]):
			return 0
		
		if ReFig[LocX][LocY] != -1:
			return 0
		if Tobimg[LocX][LocY] != Node:
			return 1

		#print([Tobimg[LocX][LocY], Node])
		if BFS(LocX + 1, LocY, Tobimg[LocX][LocY]) == 1:
			ReFig[LocX][LocY] = 255
		else:
			ReFig[LocX][LocY] = 0
		
		if BFS(LocX, LocY + 1, Tobimg[LocX][LocY]) == 1:
			ReFig[LocX][LocY] = 255
		elif ReFig[LocX][LocY] == -1:
			ReFig[LocX][LocY] = 0
		return 0


	for i in range(0, len(Tobimg)):
		for j in range(0, len(Tobimg[i])):
			if ReFig[i][j] != -1:
				continue
			else:
				if BFS(i + 1, j, Tobimg[i][j]) == 1:
					ReFig[i][j] = 255
				else:
					ReFig[i][j] = 0
				
				if BFS(i, j + 1, Tobimg[i][j]) == 1:
					ReFig[i][j] = 255
				elif ReFig[i][j] == -1:
					ReFig[i][j] = 0
					
	Init.LogWrite("Figure iterator succeed","0")
	
	return ReFig


def Main(img):
	print(GetEnp(img))
	img = GetBoundary(Toboggan(img))
	print(GetEnp(img))

	return img

