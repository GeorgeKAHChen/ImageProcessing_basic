#=================================================================
#
#		Image Processing - Proj3
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
from PIL import ImageFilter

#import files
import Convolution
import Proj2
def UM(img):
	#Unsharp masking and high-boost filtering
	Kernel = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) / 25
	img2 = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	img1 = Convolution.D2FFT(img, Kernel)
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img2[i][j] = img[i][j] - img1[i][j]
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = img[i][j] + img2[i][j]
	return img

def BlockAlg(img):
	len1 = int(len(img) / 100)-1
	len2 = int(len(img[0]) / 100)-1
	
	img2 = [[0 for n in range(len(img[0]))] for n in range(len(img))]
	for i in range(0, len1):
		for j in range(0, len2):
			fig = [[0 for n in range(100)] for n in range(100)]
			for p in range(0, len(fig)):
				for q in range(0, len(fig[1])):
					fig[p][q] = img[i*100+p][j*100+q]
			Kernel = np.array([[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4],[1, 4, 7, 4, 1]]) / 273
			fig = Convolution.D2FFT(fig, Kernel)
			fig = Proj2.SO(fig)

			for p in range(0, len(fig)):
				for q in range(0, len(fig[p])):
					img2[i*100+p][j*100+q] = fig[p][q]

		print([i, len1])
	return img2









