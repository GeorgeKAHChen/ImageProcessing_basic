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

def UM(img):
	#Unsharp masking and high-boost filtering
	Kernel = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) / 25
	img1 = Convolution.D2FFT(img, Kernel)
	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			img[i][j] = img[i][j] + 5*img1[i][j]
	return img