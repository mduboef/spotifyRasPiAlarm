import pyautogui
import time
import datetime
#from datetime import datetime

alarmTime1 = datetime.time(9,29,00)
debug = False

alarmTime = alarmTime1.strftime("%H:%M")
print(alarmTime)

# infinite loop printing position for debug
i = 1
if debug == True:
	while 1:
		i += 1
		print(pyautogui.position())

# infinite loop for alarm running
while 1:

	# update current time
	now = datetime.now()
	timeNow = now.strftime("%H:%M")
	
	print(timeNow)

	# alarm time
	if timeNow == alarmTime:
		
		#OPEN BROWSER
		pyautogui.moveTo(20,20,1)
		pyautogui.click()
		pyautogui.moveTo(80,168,1)
		pyautogui.moveTo(284,166,1)
		pyautogui.click()
		time.sleep(10)
		
		#OPEN DAILY DRIVE
		pyautogui.moveTo(222,148,1)
		pyautogui.click()
		time.sleep(25)
		
		#PLAY SONG 1
		pyautogui.moveTo(288,811,1)
		pyautogui.click()
		time.sleep(5)
		
		#QUEUE NPR NEWS
		pyautogui.moveTo(1860,755,1)
		pyautogui.click()
		time.sleep(1)
		pyautogui.moveTo(1730,780,1)
		pyautogui.click()
		time.sleep(5)
		
		#QUEUE SONG 2
		pyautogui.moveTo(1860,866,1)
		pyautogui.click()
		time.sleep(1)
		pyautogui.moveTo(1689,524,1)
		pyautogui.click()
		time.sleep(5)

		#OPEN NEW TAB
		pyautogui.moveTo(269,80,1)
		pyautogui.click()
		time.sleep(10)
		
		#OPEN NYT DAILY
		pyautogui.moveTo(155,148,1)
		pyautogui.click()
		time.sleep(25)
		
		#QUEUE NYT DAILY
		pyautogui.moveTo(1214,759,1)
		pyautogui.click()
		time.sleep(1)
		pyautogui.moveTo(1300,788,1)
		pyautogui.click()
		
		pyautogui.moveTo(0,0,1)

		#CLOSE BROWSER
		time.sleep(5400)
		pyautogui.moveTo(1905,49)
		pyautogui.click()
	
	# if not alarm time wait 59 seconds
	else:
		time.sleep(59)
	
