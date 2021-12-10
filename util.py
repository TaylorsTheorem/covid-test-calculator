import json

def get_data():
    with open("data.txt", "r") as datafile:
        return json.loads(datafile.read())

def get_district_list():
    with open("district_list.txt", "r") as datafile:
        return json.loads(datafile.read())
    
