import pyautogui
import time
import datetime

# wake up time in 24 hr format
alarmHour = 8
alarmMin = 59

debug = False

# infinite loop printing position for debug
i = 1
if debug == True:
	while True:
		i += 1
		print(pyautogui.position())
		
print("Alarm set for " + str(alarmHour) + ":" + str(alarmMin))

# infinite loop for alarm running
while True:

	# check if it is alarm time
	if  alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
		
		print("Good morning Mason, you absolute smokeshow.")
		time.sleep(5)
		
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
	
