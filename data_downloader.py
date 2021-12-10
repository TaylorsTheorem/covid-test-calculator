import requests, json


''' 
    Request and output RKI data into 'data.txt' file. 
    This code comes from https://arcgis.esri.de/nutzung-der-api-des-rki-covid-19-dashboard/
'''

url = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/rki_admunit_v/FeatureServer/0/query?"
parameter = {
'referer':'https://www.akar.de',
    'user-agent':'python-requests/2.9.1',
    'where': '1=1', # Alle Status-Datensätze
    'outFields': '*', # Rückgabe aller Felder
    'returnGeometry': False, # Keine Geometrien
    'f':'json', # Rückgabeformat, hier JSON
'cacheHint': True # Zugriff über CDN anfragen
}

result = requests.get(url=url, params=parameter) #Anfrage absetzen
resultjson = json.loads(result.text) # Das Ergebnis JSON als Python Dictionary laden

district_list = dict()
for district in resultjson["features"]:
    district_list[district["attributes"]["AdmUnitId"]] = district["attributes"]["Name"]

# with open("district_list.txt", "w") as outfile:
#     json.dump(district_list, outfile)



url = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/rki_key_data_v/FeatureServer/0/query?"
parameter = {
'referer':'https://www.akar.de',
    'user-agent':'python-requests/2.9.1',
    'where': '1=1', # Alle Status-Datensätze
    'outFields': '*', # Rückgabe aller Felder
    'returnGeometry': False, # Keine Geometrien
    'f':'json', # Rückgabeformat, hier JSON
'cacheHint': True # Zugriff über CDN anfragen
}

result = requests.get(url=url, params=parameter) #Anfrage absetzen
resultjson = json.loads(result.text) # Das Ergebnis JSON als Python Dictionary laden

data = []
for i, val in enumerate(resultjson["features"]):
    data.append(val["attributes"])
    del(data[i]["ObjectId"])

for district in data:
    district["Name"] = district_list[district["AdmUnitId"]]

with open("data.txt", "w") as outfile:
    json.dump(data, outfile)
