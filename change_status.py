import requests
import json

USER_TOKEN = "xoxp-*****"
USER_ID = "*****"

def main(text,emoji):
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
	print(res.url)

if __name__ == '__main__':
	main("研究室",":office:")