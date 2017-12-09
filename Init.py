############################################################
#
#		Some useful function
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Init.py
#
############################################################
"""
LogWrite(LogStr, kind)
	This function will write the infomation into the log file.
	
	LogStr = "Infomation You want to add"
	kind = "0" #The program worked right
	kind = "else" #ERROR else

	return None

BuildFile(FileName)
	NOTE: THIS FUNCTION MAY CANNOT USE IN WINDOWS SYSTEM!!
	This function will build a new file with FileName

	FileName = "The name of the file you want to build"

	return None

IntInput(Str, Min, Max, Method)
	This function will judge the input string.

	Str = "The infomation which will print"
	Min = the min of input (int / float / inf)
	Max = the max of input (int / float / inf)
	Method = "The kind of input data you need" (int / float) 
	
	return InputNumber

GetTime()
	This function will return the time as a int

	return Time

ArrOutput(Arr):
	This function will save the array as a table.

	Arr = The array you want to save

	return None

GetNextDay(Time, TimeAdd)
	This function will calculated the next day by the calendar

	Time = 19961221 (The beginning time)
	TimeAdd = 3 (The time you want to add)

	return Time+TimeAdd
"""


#FileName = Init.py
#Kazuki Amakawa

#Initialization file
#Init.LogWrite(LogStr, kind)
#Init.BuildFile(FileName)
import TimeCal

def LogWrite(LogStr, kind):
	import os
	import time 
	FileName = "CRIEA.log"

	FileName = "IMP.log"
		
	File = open(FileName, "a")
	Ima = time.ctime()
	WriteStr = '[' + Ima + ']'
	if kind == '0':
		WriteStr = WriteStr + '  Info   '
	else:
		WriteStr = WriteStr + '  Error  '
	WriteStr = WriteStr + LogStr + '\n'
	File.write(WriteStr)
	File.close()
	return 0


def BuildFile(FileName):
	import os
	if not os.path.exists(FileName):
		os.system("cat /dev/null > " + str(FileName))
	Str = FileName + 'build succeed'
	LogWrite(Str, '0')



def GetAveSqr(Arr):
	TTL = 0
	for i in range(0, len(Arr)):
		TTL += Arr[i]

	Ave = TTL / len(Arr)

	TTL2 = 0
	for i in range(0, len(Arr)):
		TTL2 += pow((Arr[i] - Ave), 2)
	
	Sqr = TTL2 / len(Arr)

	return [TTL, Ave, Sqr]


def ArrOutput(Arr):
	FileName = "SaveArr" + str(TimeCal.GetTime())
	BuildFile(FileName)
	File = open(FileName, "a")
	Str = ""
	for i in range(0, len(Arr)):
		for j in range(0, len(Arr[i])):
			Str += str(Arr[i][j])
			Str += "\t"
		Str += "\n"
	File.write(Str)
	File.close()



def IntInput(Str, Min, Max, Method):
	Int = 0
	NoMin = False
	NoMax = False
	try:
		Min = int(Min)
	except:
		NoMin = True

	try:
		Max = int(Max)
	except:
		NoMax = True
	
	while 1:
		InpStr = input(Str)
		try:
			if Method == "int":
				Int = int(InpStr)
			elif Method == "float":
				Int = float(InpStr)
		except:
			print("Input Error")
			continue
		else:
			if NoMin == True and NoMax == True:
				break
			
			elif NoMin == True and NoMax == False:
				if Int > Max:
					print("Input Error")
					continue
				else:
					break
		
			elif NoMin == False and NoMax == True:
				if Int < Min:
					print("Input Error")
					continue
				else:
					break
			else:
				if Int < Min or Int > Max:
					print("Input Error")
					continue
				else:
					break
	return Int



def GetTime():
	import time
	TimeStr = time.ctime()
	TimeStr += ' '
	Space = -1
	Jikan = ['', '', '', '']
	RemStr = ''
	for i in range (0, len(TimeStr)):
		if TimeStr[i] == ' ':
			if RemStr == '':
				continue
			else:
				if not Space == -1:
					Jikan[Space] += RemStr
				RemStr = ''
				Space += 1	
		else:
			RemStr += TimeStr[i]

	ReturnTime = 0
	try:
		ReturnTime = int(Jikan[3])
	except ValueError:
		LogWrite('Get time error', '121')
		return -1
	ReturnTime *= 100

	if Jikan[0] == "Jan":
		ReturnTime += 1
	if Jikan[0] == "Feb":
		ReturnTime += 2
	if Jikan[0] == "Mar":
		ReturnTime += 3
	if Jikan[0] == "Apr":
		ReturnTime += 4	
	if Jikan[0] == "May":
		ReturnTime += 5
	if Jikan[0] == "Jun":
		ReturnTime += 6
	if Jikan[0] == "Jul":
		ReturnTime += 7
	if Jikan[0] == "Aug":
		ReturnTime += 8	
	if Jikan[0] == "Sep":
		ReturnTime += 9
	if Jikan[0] == "Oct":
		ReturnTime += 10
	if Jikan[0] == "Nov":
		ReturnTime += 11
	if Jikan[0] == "Dec":
		ReturnTime += 12

	ReturnTime *= 100

	try:
		ReturnTime += int(Jikan[1])
	except ValueError:
		LogWrite('Get time error', '122')
		return -1

	ReturnTime *= 1000000
	DokiStr = ''
	Kanryou = 0
	for i in range (0, len(Jikan[2])):
		if Jikan[2][i] == ':':
			Kanryou += 1
			if Kanryou == 1:
				continue
			else:
				try:
					ReturnTime += int(DokiStr)
				except ValueError:
					LogWrite('Get time error', '123')
					return -1
				break
			
		else:
			DokiStr += Jikan[2][i]

	return ReturnTime


def ArrOutput(Arr):
	FileName = "SaveArr" + str(GetTime())
	BuildFile(FileName)
	File = open(FileName, "a")
	Str = ""
	for i in range(0, len(Arr)):
		for j in range(0, len(Arr[i])):
			Str += str(Arr[i][j])
			Str += "\t"
		Str += "\n"
	File.write(Str)
	File.close()


def GetNextDay(Time, TimeAdd):
	Day = Time % 100
	Mouth = ((Time - Day)/100) % 100
	Year = int(Time / 10000)
	Day += TimeAdd
	
	if Mouth == 2:
		if Year % 400 == 0 or (Year % 100 != 0 and Year % 4 == 0):
			if Day > 29:
				Day -= 29
				Mouth += 1
		else:
			if Day > 28:
				Day -= 28
				Mouth += 1

	if Mouth == 1 or Mouth == 3 or Mouth == 5 or Mouth == 7 or Mouth == 8 or Mouth == 10:
		if Day > 31:
			Day -= 31
			Mouth += 1
	
	if Mouth == 4 or Mouth == 6 or Mouth == 9 or Mouth == 11:
		if Day > 30:
			Day -= 30
			Mouth += 1
	
	if Mouth == 12:
		if Day > 31:
			Day -= 31
			Mouth = (Mouth + 1) % 12
			Year += 1

	return (Year * 10000 + Mouth * 100 + Day)



