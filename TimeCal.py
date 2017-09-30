#FileName = TimeCal.py
#By Kazuki Amakawa
#Time Calculation
#TimeCal.GetTime() = Output the time at present as year mouth day hour minute in an internal
#TimeCal.GetNextDay(DayBefore, Day) = year mouth day internal + Day 

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

	ReturnTime *= 10000
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



#================================================================================================================