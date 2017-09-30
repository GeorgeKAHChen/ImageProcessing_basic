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

def GetGradient(img):
	GraArr = [0 for n in range(260)]

	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			try:
				GraArr[abs(img[i+1][j] - img[i][j])] += 1
				GraArr[abs(img[i][j+1] - img[i][j])] += 1
			except:
				continue

	#Establish the figure
	fig1 = plt.figure()
	ax = fig1.add_subplot(111)
	
	#x y lim setting	
	plt.xlim(0, 256)
	plt.ylim(0, pow(len(img), 2) / 2)

	#Printing loop
	for i in range(0, len(GraArr)):
		ax.add_patch(patches.Rectangle((i, 0), 1, GraArr[i], color = 'black'))

	#Saving and output
	fig1.show()
	Init.LogWrite("Gradient Figure Output succeed", "0")
	input('Press Enter key to continue')
	return


def GT(img):
	#Thresholding with Gradient
	img1 = [[0 for n in range(len(img[0])+10)] for n in range(len(img) + 10)]
	img1 [0][0] = 0
	for i in range(0, len(img)):
		try:
			if (abs(img[i+1][0] - img[i][0])) > 128:
				if img[i][j] == 0:
					img1[i+1][0] = 255
				else:
					img1[i+1][0] = 0
			else:
				img1[i+1][j] = img1[i][j]
		except:
			continue

	for i in range(0, len(img)):
		for j in range(0, len(img[i])):
			try:
				if (abs(img[i][j+1] - img[i][j])) > 128:
					if img1[i][j] == 0:
						img1[i][j+1] = 255
					else:
						img1[i][j+1] = 0
				else:
					img1[i][j+1] = img1[i][j]
			except:
				continue
	Init.LogWrite("Gradient Figure Calculation succeed", "0")
	return img1
