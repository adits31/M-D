import requests
import json
with open('data.json') as data_file:
	data = json.load(data_file)
	headers = {'content-type': 'text/plain'}
	resp = requests.post("https://www.googleapis.com/prediction/v1.6/projects/mood-182211/trainedmodels/language-identifier/predict?key=AIzaSyCo1IFNRMqjdKT8Ka0FQ9caVEtnxySjsO8",
				json=data)
	print(resp.content)