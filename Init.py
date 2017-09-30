#FileName = Init.py
#Kazuki Amakawa

#Initialization file
#Init.LogWrite(LogStr, kind)
#Init.BuildFile(FileName)
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



#================================================================================================================
