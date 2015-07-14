# main.py -- put your code here!

# main.py -- put your code here!

try:
	from pyb import *

	LS = Pin('X5', Pin.IN)
	Lservo = Servo(2)
	Rservo = Servo(1)
	red = Pin('Y6', Pin.OUT_PP)
	blue = Pin('Y4', Pin.OUT_PP)
	button = Pin('Y1', Pin.IN)
	

	def stop():
		LED(1).on()
		LED(2).off()
		LED(3).off()
		red.low()
		blue.low()
		Rservo.speed(-1)
		Lservo.speed(0)
		
	def moveStraight():
		Rservo.speed(-10)
		Lservo.speed(8.1)
		
	def turnRight():
		Rservo.speed(-1)
		Lservo.speed(17)
		
	def turnLeft():	
		Rservo.speed(-19)
		Lservo.speed(0)
			
	def tracker():
		stop()
		buttonValue, currentState = 1, False
		while True:
			LSvalue = LS.value()
			newButtonValue = button.value()
			if LSvalue == 1 and currentState:
				LED(1).off()
				LED(2).on()
				LED(3).off()
				moveStraight()
				red.low()
				blue.high()
				#delay(100)
			elif currentState:
				LED(1).off()
				LED(3).on()
				LED(2).off()
				turnRight()
				blue.low()	
				red.high()
				#delay(100)

			if newButtonValue != buttonValue:
				buttonValue = newButtonValue
				currentState = not currentState if buttonValue == 0 else currentState
				if not currentState:
					stop()
				
		
	def lights():
		while True:
			LSvalue = LS.value()
			if LSvalue == 1:
				LED(2).on()
				LED(3).off()
			else:
				LED(3).on()
				LED(2).off()

	tracker()
except BaseException as errString:
	f = open('errorLog.txt', 'w')
	f.write(str(errString))
	f.close()
