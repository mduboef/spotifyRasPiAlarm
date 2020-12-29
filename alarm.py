import pyautogui
import time
import datetime

# wake up time in 24 hr format
alarmHour = 7
alarmMin = 59

debugMode = False

# infinite loop printing position for debug
while debugMode == True:
	print(pyautogui.position())
		
print("Alarm set for " + str(alarmHour) + ":" + str(alarmMin))

# infinite loop for alarm running
while True:

	# check if it is alarm time
	if  alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
		
		print("Good morning Mason, you absolute smokeshow.")
		
		#WAKE UP SCREEN
		pyautogui.click()
		pyautogui.moveTo(10,10,1)
		pyautogui.moveTo(500,500,1)
		pyautogui.moveTo(10,10,1)
		pyautogui.moveTo(500,500,1)
		pyautogui.moveTo(10,10,1)
		pyautogui.moveTo(500,500,1)
		time.sleep(5)
		
		#OPEN BROWSER
		pyautogui.moveTo(12,1071,1)
		pyautogui.click()
		pyautogui.moveTo(123,780,1)
		pyautogui.moveTo(288,785,1)
		pyautogui.click()
		time.sleep(15)
		
		#OPEN DAILY MIX
		pyautogui.moveTo(294,113,1)
		pyautogui.click()
		time.sleep(25)
		
		#PLAY SONG 1
		pyautogui.moveTo(288,624,1)
		pyautogui.click()
		time.sleep(5)
		
		#OPEN DAILY DRIVE
		pyautogui.moveTo(270,46,1)
		pyautogui.click()
		time.sleep(5)
		pyautogui.moveTo(228,112,1)
		pyautogui.click()
		time.sleep(25)
		
		#QUEUE NPR NEWS
		pyautogui.moveTo(1862,726,1)
		pyautogui.click()
		time.sleep(1)
		pyautogui.moveTo(1747,750,1)
		pyautogui.click()
		time.sleep(5)
		
		#QUEUE SONG 2
		pyautogui.moveTo(91,42,1)
		pyautogui.click()
		pyautogui.moveTo(1861,681,1)
		pyautogui.click()
		time.sleep(1)
		pyautogui.moveTo(1706,338,1)
		pyautogui.click()
		time.sleep(5)

		#OPEN NYT DAILY
		pyautogui.moveTo(507,44,1)
		pyautogui.click()
		time.sleep(10)
		pyautogui.moveTo(148,111,1)
		pyautogui.click()
		time.sleep(25)
		
		#QUEUE NYT DAILY
		pyautogui.moveTo(1214,722,1)
		pyautogui.click()
		time.sleep(1)
		pyautogui.moveTo(1303,747,1)
		pyautogui.click()
		time.sleep(5)
		
		pyautogui.moveTo(10,10,1)

		#CLOSE BROWSER
		time.sleep(5000)
		pyautogui.moveTo(1906,14)
		pyautogui.click()
	
	# if not alarm time wait 59 seconds
	else:
		time.sleep(10)
	
