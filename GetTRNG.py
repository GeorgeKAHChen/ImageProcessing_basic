######################################################################################
##
##		Dioxins Absorption and Desorption Model(DADM)
##		Get_Random_General
##		By Kazuki Amakawa
##		Source: https://github.com/KazukiAmakawa/Dioxins-Absorption-and-Desorption-Model/blob/master/GetRandom.py
##
######################################################################################
'''
#------------Output File: RandomNumberList
This program will get a confident random generation by the moving mouse
It is a part of my paper when I study Probability and Statistic,
so it is independence of the main function
It will used before the main program is begin, and will output the random list
for the main calculation
'''
#Initialization the import file we need 
from tkinter import *
import time
import tkinter as tank
import os
import Init
owari = 0

def MainFunction(TOTAL):
	#Variable Initial
	Begin_Time = time.clock()

	#Initialization the array to remember the location
	TRNGx = []
	TRNGy = []

	#Waiting for the system begin
	print("Now, begin to move your mouse quickly until the window is closed.")
	time.sleep(1)

	#Begin the main pro window
	root = tank.Tk()

	#Initial the window
	#The title of the window
	root.title("The System of Generating TRNG")
	#The floor of the window
	root.wm_attributes('-topmost',1)
	#The size of the window
	root.wm_state( 'zoomed' )

	global owari
	owari = int(TOTAL)+20
	#The main function to get the local of window
	def motion(event):
		#Get the Location of mouse
		TRNGx.append(event.x)
		TRNGy.append(event.y)

		#To exit the window while the point are enough
		global owari
		owari -= 1

		if owari == 0:
			root.quit()

	#Define the function into the mainloopG
	root.bind('<Motion>', motion)

	#Begin the mainloop
	root.mainloop()

	#Open the File to write
	FileName1 = "RandomNumberList"
	if os.path.exists(FileName1):
		os.remove(FileName1)
		Init.BuildFile(FileName1)
	else:
		Init.BuildFile(FileName1)
	File = open(FileName1, 'w')

	#The Function mix both CPU clock and mouse local
	def Calculation(InpNum):
		TimeVal = []
	#Get the time string of CPU clock
		TimeVal = str(time.clock() - Begin_Time)
	#Add the last of TimeVal and the InpNum
		Finout = str((int(TimeVal[len(TimeVal)-1]) + InpNum) % 10)
	#Write the string into the file
		File.write(Finout)

	def FileJudge(FileName):
		import os
		if not os.path.exists(FileName):
			os.mknod(FileName)
		if os.path.exists(FileName):
			return 0
		else:
			Init.LogWrite("Build file error", "101")
			exit()

	#The loop of Final calculation and output
	for i in range(0, int(TOTAL)):
		Calculation(TRNGx[i])
		Calculation(TRNGy[i])

	#Save and Close the File and End the program
	File.close()

#================================================================================================================