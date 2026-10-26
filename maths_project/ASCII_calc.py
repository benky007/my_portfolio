import os
import time
from full import start_up, title, left
trys = 0
z = 0
start_up()
while True:
	def binary():
		title()
		a = input('What statement do you want to be turned into binary?\n')
		b = int(len(a))
		time.sleep(1)
		os.system('clear')
		title()
		for i in range(b):
			print(bin(ord(a[i]))[2:])
		time.sleep(b*2)
		os.system('clear')
		title()
		
	def hexadecimal():
		title()
		c = input('What statement do you want to be turned into hexadecimal?\n')
		d = int(len(c))
		time.sleep(1)
		os.system('clear')
		title()
		for x in range(d):
			print(hex(ord(c[x]))[2:])
		time.sleep(d*2)
		os.system('clear')
		title()
			
	def octal():
		title()
		e = input('What statement do you want to be turned into octal?\n')
		f = int(len(e))
		time.sleep(1)
		os.system('clear')
		title()
		for y in range(f):
			print(oct(ord(e[y]))[2:])
		time.sleep(f*2)
		os.system('clear')
		title()
	
	def help():
		time.sleep(1)
		os.system('clear')
		print('\n------------------------------------------------------------\n                            HELP                                     \n\nAll that you need to do is pick one of: hexadecimal, binary or octal. And then all you need to do is write your\nstatement and the program will automatically turn your\nstatement into which ever one of the three number systems\nabove.\n------------------------------------------------------------\n')
		time.sleep(7.5*2)
		os.system('clear')
		title()
	os.system('clear')
	title()
	e = input('Would you like to turn your statement into binary\nhexadecimal octal or would you rather leave the program?\n')

	if e.lower() == 'hexadecimal':
		os.system('clear')
		hexadecimal()
	elif e.lower() == 'binary':
		os.system('clear')
		binary()
	elif e.lower() == 'octal':
		os.system('clear')
		octal()
	elif e.lower() == 'help':
		os.system('clear')
		help()
	elif e.lower() == 'leave':
		os.system('clear')
		left()
		time.sleep(1)
		break
	else:
		trys += 1
		if trys == 3:
			time.sleep(1)
			os.system('clear')
			title()	
			print('How stupid are you? Heres some help')
			time.sleep(1)
			os.system('clear')
			title()
			help()
		elif trys == 5:
			time.sleep(1)
			os.system('clear')
			title()
			print('\nYou are officially dubbed STUPID!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
			time.sleep(5)
			os.system('clear')
			title()
			break
		else:
			time.sleep(1)
			os.system('clear')
			title()
			print('Try again\n\n\n')
			time.sleep(1)
			os.system('clear')
			title()
