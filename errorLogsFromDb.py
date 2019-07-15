import json
import requests
import sys

if len(sys.argv) < 4:
	print("Table name, search query and user cookie is required")
else:
	tableName = sys.argv[2]
	query = sys.argv[3]
	USER_COOKIE = sys.argv[1]
	BOTID = "x1532195756954"
	import requests

	url = "https://app.yellowmessenger.com/api/data/data/search/"+ tableName +"/0-12"

	querystring = {"bot": BOTID,"field":"*","query": query}

	headers = {
    	'x-auth-token': USER_COOKIE,
    	'Cache-Control': "no-cache",
    }

	response = requests.request("GET", url, headers=headers, params=querystring)

	record = json.loads(response.text)

	if (record['success'] != True):
		print('No response')
	elif len(record['data']['records']) == 0:
		print('There are no records regards your query: ', query)
		print(record)
	else:
		record = record['data']['records'][0]
		request = json.loads(record['request'])
		response = record['response']
		with open(tableName + '_' + query + '.txt', 'w') as file:
			file.write('Request: ')
			file.write(request['body'])
			file.write('Reponse:\n')
			file.write(response)
			file.close()
print('Done writing to file ', tableName+'_'+query+'.txt')