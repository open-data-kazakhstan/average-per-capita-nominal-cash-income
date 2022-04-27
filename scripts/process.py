import json
import requests
import csv

r = requests.get('https://taldau.stat.gov.kz/ru/Api/GetIndexData/2709380?period=7&dics=67')

raw_dt = json.loads(r.text)

with open('data/output.csv', 'w', newline='') as file:
    fieldnames = ['city', 'date', 'value']
    writer = csv.writer(file)
    writer.writerow(fieldnames)
    for i in raw_dt:
        for j in range(len(i["periods"])):
            writer.writerow((i["termNames"][0],i["periods"][j]['date'],i["periods"][j]['value']))
            