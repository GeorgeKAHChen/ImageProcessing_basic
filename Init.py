#FileName = Init.py
#Kazuki Amakawa

#Initialization file
#Init.LogWrite(LogStr, kind)
#Init.BuildFile(FileName)
import TimeCal

def LogWrite(LogStr, kind):
	import os
	import time 
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




