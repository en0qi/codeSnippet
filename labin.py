import RPi.GPIO as GPIO
from time import sleep
import datetime
import requests
import json

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
status = 0
onlab = 0

USER_TOKEN = "xoxp-******"
USER_ID = "********"

def change_status(text,emoji):
	param = {
	"token" : USER_TOKEN,
	"user": USER_ID,
	"profile":json.dumps({
		"status_text":text,
		"status_emoji":emoji
		})
	}
	res = requests.post('https://slack.com/api/users.profile.set',params = param)
	print(res.text)

try:
	while True:
		GPIO.wait_for_edge(12, GPIO.FALLING)
		if onlab == 0:
			onlab = 1
			change_status("ラボ",":office:")
			dt_in = datetime.datetime.now()
			dt_str_in = dt_in.strftime('%H:%M:%S')
			GPIO.output(16,GPIO.HIGH)
			print("研究室 IN  {}".format(dt_str_in))
			requests.post('https://hooks.slack.com/services/*******', data = json.dumps({
			 'text': "<@********> さんが *研究室 IN* しました。 \n入室時刻 {}".format(dt_str_in), 
			 'username': 'なおこ', 
			 'link_names': 1, 
			 }))
			#IFTTT URL for Logging to Google Sheets
			IFTTT_URL_GoogleSheets = 'https://maker.ifttt.com/trigger/roomba/with/key/'
			# IFTTT Key
			IFTTT_KEY = '********'
			requests.post(IFTTT_URL_GoogleSheets + IFTTT_KEY, json = {'value1':'IN','value2':'','value3':''})
			sleep(1)
		elif onlab == 1:
			onlab = 0
			change_status("","")
			dt_out = datetime.datetime.now()
			dt_len = dt_out - dt_in
			dt_str_out = dt_out.strftime('%H:%M:%S')
			dt_str_len = str(dt_len).split(".")[0]
			GPIO.output(16,GPIO.LOW)
			print("研究室 OUT  {}".format(dt_str_out)+"\n滞在時間 "+dt_str_len)
			requests.post('https://hooks.slack.com/services/*******', data = json.dumps({
			 'text': "<@********> さんが *研究室 OUT* しました。 \n入室時刻 {}\n退室時刻 {}".format(dt_str_in,dt_str_out)+"\n滞在時間 "+dt_str_len, 
			 'username': 'なおこ', 
			 'link_names': 1, 
			 }))
			# IFTTT URL for Logging to Google Sheets
			IFTTT_URL_GoogleSheets = 'https://maker.ifttt.com/trigger/roomba/with/key/'
			# IFTTT Key
			IFTTT_KEY = '********'
			requests.post(IFTTT_URL_GoogleSheets + IFTTT_KEY, json = {'value1':'OUT','value2':'{}'.format(dt_str_len),'value3':''})
			sleep(1)
		sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()
	print("cleaned")
