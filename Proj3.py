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
import cv2

#import files
import Convolution

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