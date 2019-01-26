# freshman_work of Groupware lab. 
# Yuki NOAKI 2018-04-10
# University of Tsukuba 

import RPi.GPIO as GPIO
import time
import serial
import requests
import json
from time import sleep
import serial
import datetime

TOKEN = "xoxb-*****"
TRIG = 21 #dist sensor
ECHO = 20 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def motion_detect():
	# try:
		# while True:
	GPIO.setup(18, GPIO.IN) #motion sensor
	return GPIO.input(18)
	# sleep(1)
	# except KeyboardInterrupt:
	# 	pass

def reading(sensor):
	global TRIG
	global ECHO
	# GPIO.setmode(GPIO.BCM)
	if sensor == 0:
		GPIO.setup(TRIG,GPIO.OUT)
		GPIO.setup(ECHO,GPIO.IN)
		GPIO.output(TRIG, GPIO.LOW)
		# time.sleep(0.3)
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO) == 0:
			signaloff = time.time()

		while GPIO.input(ECHO) == 1:
			signalon = time.time()

		timepassed = signalon - signaloff
		distance = timepassed * 17000
		return distance
		GPIO.cleanup()
	else:
		# print "Incorrect usonic() function varible."
		pass
	# GPIO.cleanup()

def post2slack(status):
	dt_in = datetime.datetime.now()
	dt_str_in = dt_in.strftime('%H:%M:%S')
	requests.post('https://hooks.slack.com/services/****', data = json.dumps({
	 'text': "<@*****> さんが *研究室 {}* しました。 \n時刻 {}".format(status,dt_str_in), # 投稿するテキスト
	 'username': 'なおこ', # 投稿のユーザー名
	 'link_names': 1, # メンションを有効にする
	 }))
	# IFTTT URL for Logging to Google Sheets
	IFTTT_URL_GoogleSheets = 'https://maker.ifttt.com/trigger/roomba/with/key/'
	# IFTTT Key
	IFTTT_KEY = '*****'
	if status == "IN":
		params = {
		"token" : TOKEN,
		"user":"*****",
		"status_text":"labo",
		"status_emoji":":office:"
		}
	else:
		params = {
		"token" : TOKEN,
		"user":"*****",
		"status_text":"",
		"status_emoji":""
		}
	requests.post('https://slack.com/api/users.profile.set',json = params)
	requests.post(IFTTT_URL_GoogleSheets + IFTTT_KEY, json = {'value1':'{}'.format(status),'value2':'','value3':''})

if __name__ == '__main__':
	status = 0
	instatus = 0
	waittime = 300
	try:
		while True:
			dist = reading(0)
			motion = motion_detect()
			print("dist:{} motion:{}".format(dist,motion))
			if dist != None:
				if float(dist) > 100 and motion == 0.0:
					print("外出判定")
					status += 1
					if status == waittime:
						status = 0
						instatus = 0
						post2slack("OUT")
						# break
					else:
						print("外出 Last {}/{}秒".format(waittime - status,waittime))
						# pass
				else:
					print("ラボにいる Last {}/{}秒".format(waittime - instatus,waittime))
					instatus += 1
					if instatus == waittime:
						post2slack("IN")
				# pass
			time.sleep(1.0)
	except Exception as e:
		print("=*= Error =*=")
				# IFTTT URL for Logging to Google Sheets
		IFTTT_URL_GoogleSheets = 'https://maker.ifttt.com/trigger/roomba/with/key/'
		# IFTTT Key
		IFTTT_KEY = '*****'
		requests.post(IFTTT_URL_GoogleSheets + IFTTT_KEY, json = {'value1':'Err','value2':'','value3':'{}'.format(e)})
	# finally:





