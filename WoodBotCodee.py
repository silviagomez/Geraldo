# main.py -- put your code here!
#original code for Geraldo, in short the first line-following following code

from pyb import *


LS = Pin('X5', Pin.IN)
Rservo = Servo(1)
Lservo = Servo(2)
red = Pin('Y6', Pin.OUT_PP)
blue = Pin('Y4', Pin.OUT_PP)

def stop():
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
	while True:
		LSvalue = LS.value()
		if LSvalue == 1:
			LED(2).on()
			LED(3).off()
			turnLeft()
			red.low()
			blue.high()
			#delay(100)
		else:
			LED(3).on()
			LED(2).off()
			turnRight()
			blue.low()	
			red.high()
			#delay(100)
		

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

