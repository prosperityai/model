

#______________________________code_______________________________________

from RPLCD import CharLCD
from time import sleep


#=============== specify lcd========================
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])
lcd.clear()

#_______________welcome_____________


lcd.write_string(u'Welcome')
sleep(1)
lcd.clear()
lcd.write_string(u'Waiting for signal')


def show_results(makeup_type):	
	#_______________showing the makeup result_________________
	try:	lcd.clear()
		makeup_message = 'Recommended make up\n\rYou Need\n\rMakeup type '+makeup_type
		print(makeup_message)
		lcd.write_string(makeup_message)
		sleep(1)
		print('displayed on the lcd screen')
	except Exception as ex:
		print(ex)
		print("The above error have occured")
		
#____________________________end code___________________________________________



