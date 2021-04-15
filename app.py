import pandas as pd
import requests
import json
from datetime import datetime

BOTID = ""
TABLE = ""
TOKEN = ""
URL = ""

HEADERS = {
    'x-auth-token': TOKEN,
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "a7d88b37-990e-4c9d-b0a6-fcaf9f6af5ce"
}


df = pd.read_csv('payment_links_july_2019.csv')
df.fillna(0, inplace=True)
print("Total Count", df.count())
START = 0
OFFSET = 5000
COLUMNS = list(df)
FLAG = True

print('This are headers : ', COLUMNS)
proceed = input('Do you want me to prooceed (y/n) : ')

def generateRow(row):
    formattedRow = {}
    for (index, value) in enumerate(COLUMNS):
        if row[index]:
            formattedRow[value] = row[index]
        else:
            formattedRow[value] = ""
    formattedRow["insertedDate"] = datetime.now().isoformat()
    return formattedRow

def uploadRows(links):
    print("Uploading rows from ", len(links))
    print(links[0])
    payload = json.dumps({"table" : TABLE, "records" : links})
    querystring = {"bot": BOTID}
    response = requests.request("POST", URL, data=payload, headers= HEADERS, params=querystring)
    print()
    if response.status_code != 200:
        raise Exception(response.content)
    print("Links uploaded successfully..")

if proceed == 'y':
    while True:
        doc = df.loc[START:START + OFFSET]
        linksDict = []
        if doc.empty:
            print('....  DONE  ....')
            break
        for index, row in doc.iterrows():
            if FLAG:
                linksDict.append(generateRow(row))
            else:
                linksDict.append({'Policy_No' : row['Policy_No'], "Pay_Now_Link" : row['Email_Link'] })
        print("Uploading from " + str(START) +" to " + str((START + OFFSET)))
        uploadRows(linksDict)
        START += OFFSET
else:
    print('Good Bye...')
