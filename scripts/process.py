import json
import requests
import csv

r = requests.get('https://taldau.stat.gov.kz/ru/Api/GetIndexData/704447?period=7&dics=67')

raw_dt = json.loads(r.text)

with open('data/output.csv', 'w', newline='') as file:
    fieldnames = ['region', 'date', 'value']
    writer = csv.writer(file)
    writer.writerow(fieldnames)
    for i in raw_dt:
        for j in range(len(i["periods"])):
            dt = '{year}-{month}-{day}'.format(year = i["periods"][j]['date'].split(".")[2], month = i["periods"][j]['date'].split(".")[1], day = i["periods"][j]['date'].split(".")[0])
            writer.writerow((i["termNames"][0],dt,i["periods"][j]['value'].split(".")[0]))
            