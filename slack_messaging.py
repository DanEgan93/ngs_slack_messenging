import os
import requests
import json


test_auto_web = 'https://hooks.slack.com/services/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'
external_mess_web = 'https://hooks.slack.com/services/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'

# #slack messaging in 
def slack_message(message):
	webhook_url = external_mess_web
	slack_data = {'text': message}

	response = requests.post(
	    webhook_url, data=json.dumps(slack_data),
	    headers={'Content-Type': 'application/json'}
	)
	if response.status_code != 200:
	    raise ValueError(
	        'Request to slack returned an error %s, the response is:\n%s'
	        % (response.status_code, response.text)
	)

def slack_email(email_message):
	webhook_url = external_mess_web
	slack_data = {'text': email_message, 'as_user': True}

	response = requests.post(
	    webhook_url, data=json.dumps(slack_data),
	    headers={'Content-Type': 'application/json'}
	)
	if response.status_code != 200:
	    raise ValueError(
	        'Request to slack returned an error %s, the response is:\n%s'
	        % (response.status_code, response.text)
	)


pipeline = 'TSCP'
ws = '000001'
test = 'Run {}_{} complete'.format(ws,pipeline)
slack_message(test)
slack_email(email)

