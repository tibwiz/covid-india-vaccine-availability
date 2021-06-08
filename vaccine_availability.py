import json
import requests
import os
import time

#TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIyMmZlZTQxMy1mZDYwLTRhZjMtYTIzMC05NGJiN2Q1ODk2NWUiLCJ1c2VyX2lkIjoiMjJmZWU0MTMtZmQ2MC00YWYzLWEyMzAtOTRiYjdkNTg5NjVlIiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo5OTE2MzE1MzU1LCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjY3NzY0NzYxMTA0NDcsInVhIjoiTW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkwLjAuNDQzMC44NSBTYWZhcmkvNTM3LjM2IiwiZGF0ZV9tb2RpZmllZCI6IjIwMjEtMDUtMDFUMDA6NTE6MzYuMTg3WiIsImlhdCI6MTYxOTgzMDI5NiwiZXhwIjoxNjE5ODMxMTk2fQ.4scEVCRO4-ViCYM-LZsQrNycxFZl5kopORSLwdFJ0BE'
TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiIyMmZlZTQxMy1mZDYwLTRhZjMtYTIzMC05NGJiN2Q1ODk2NWUiLCJ1c2VyX2lkIjoiMjJmZWU0MTMtZmQ2MC00YWYzLWEyMzAtOTRiYjdkNTg5NjVlIiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo5OTE2MzE1MzU1LCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjY3NzY0NzYxMTA0NDcsInNlY3JldF9rZXkiOiJiNWNhYjE2Ny03OTc3LTRkZjEtODAyNy1hNjNhYTE0NGYwNGUiLCJzb3VyY2UiOiJjb3dpbiIsInVhIjoiTW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkwLjAuNDQzMC4yMTIgU2FmYXJpLzUzNy4zNiIsImRhdGVfbW9kaWZpZWQiOiIyMDIxLTA2LTA4VDA3OjQzOjI3LjU0OVoiLCJpYXQiOjE2MjMxMzgyMDcsImV4cCI6MTYyMzEzOTEwN30.zSin2g-5g0BkuOcG8XSvOE8KkGdYUb99QFOHxgDhKSE'

def check_appointment():
	URL='https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=304&date=09-06-2021'
	URL='https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=304&date=08-06-2021&vaccine=COVISHIELD'

	header = {'content-type': 'application/json', 'Bearer': TOKEN}

	response=requests.get(URL, headers=header, verify=False)

	print('Response received is {}'.format(response.text))

	appointments=json.loads(response.text)
	#os.system('afplay /System/Library/Sounds/Sosumi.aiff')
	for center in appointments['centers']:
		if center['sessions']:
			for session in center['sessions']:
				if session['date'] in ['08-06-2021','09-06-2021','10-06-2021','11-06-2021']:
					print("Appointment available at {} on {}".format(center['name'],session['date']))
					for i in range(10):
						os.system('afplay /System/Library/Sounds/Blow.aiff')
						time.sleep(1)


while True:
	try:
		check_appointment()
	except Exception as ex:
		print("Errrorr {}".format(ex))
	time.sleep(30)

