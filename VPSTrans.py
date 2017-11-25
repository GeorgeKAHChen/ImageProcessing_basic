#=================================================================
#
#		Image Processing - ServerTrans
#		Copyright(c) KazukiAmakawa, all right reserved.
#
#=================================================================
#import head
import numpy as np
import os
import os.path

#return img array: the array of the figure
#return -1 : exit or no figure
def Output(img):
	plt.imshow(img, cmap="gray")
	plt.axis("off")
	plt.show()
	Init.LogWrite("Figure output succeed", "0")
	InpStr = input("Save the figure?[Y/ n]")
	if InpStr == "Y" or InpStr == "y":
		Name = "Figure_"
		Name += str(TimeCal.GetTime())
		Name += ".png"
		os.system("cp null " + Name)
		misc.imsave(Name, img)
		if not os.path.exists("Output"):
			os.system("mkdir Output")
		os.system("mv " + Name + " Output/" + Name)
	return

def FigureInput():
	Figure = []
	Name = []
	root0 = ""
	for root, dirs, files in os.walk(os.getcwd()):
		if root0 == "":
			root0 = root
			root0 += "/Output"
		if root0 == root:
			continue

		for i in range(0, len(files)):
			LocStr = root + "/" + files[i]
			
			Hajimari = 0
			Last = ""

			for j0 in range(0, len(files[i])):
				j = len(files[i]) - j0 -1
				if files[i][j] == ".":
					break
				else:
					Last = files[i][j] + Last

			if Last == "bmp" or Last == "jpg" or Last == "png":
				Figure.append(LocStr)
				Name.append(files[i])

	for i in range(0, len(Figure))
		NameStr = Figure[InpInt-1]
		Ima = np.array(Image.open(NameStr).convert("L"))

	
	Init.LogWrite("Figure input succeed", "0")
	return 



