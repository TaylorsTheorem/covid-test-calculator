import requests, json

''' 
    Request and output RKI data into 'data.txt' file. 
    The request code comes from https://arcgis.esri.de/nutzung-der-api-des-rki-covid-19-dashboard/
'''

#
# Fetch district names from RKI AdmUnit Feature Server as JSON
#
url = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/rki_admunit_v/FeatureServer/0/query?"
parameter = {
'referer':'https://www.akar.de',
    'user-agent':'python-requests/2.9.1',
    'where': '1=1',
    'outFields': '*',
    'returnGeometry': False,
    'f':'json',
'cacheHint': True
}

result = requests.get(url=url, params=parameter)
resultjson = json.loads(result.text)

# Reduce resultjson to only AdmUnitId and Name key values
district_list = dict()
for district in resultjson["features"]:
    district_list[district["attributes"]["AdmUnitId"]] = district["attributes"]["Name"]


#
# Fetch data from RKI Key Data Feature Server as JSON
#

url = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/rki_key_data_v/FeatureServer/0/query?"
parameter = {
'referer':'https://www.akar.de',
    'user-agent':'python-requests/2.9.1',
    'where': '1=1',
    'outFields': '*',
    'returnGeometry': False,
    'f':'json',
'cacheHint': True
}

result = requests.get(url=url, params=parameter)
resultjson = json.loads(result.text)

# Remove unnecessary JSON blocks and only save the data of the districts
data = []
for i, val in enumerate(resultjson["features"]):
    data.append(val["attributes"])
    del(data[i]["ObjectId"])

# Add Name key value to each disctrict from district_list
for district in data:
    district["Name"] = district_list[district["AdmUnitId"]]

# Save data file
with open("data.txt", "w") as outfile:
    json.dump(data, outfile)
