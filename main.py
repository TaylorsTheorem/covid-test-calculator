import json
import util

data = util.get_data()
district_list = util.get_district_list()

def get_district_vals(data):
    for i, val in enumerate(data):
        print(i, val)
        print(type(val))

get_district_vals(data)

for i, val in enumerate(data):
    if data[i]["Name"] != district_list[i]["Name"]:
        print(data[i]["AdmUnitId"], district_list[i]["AdmUnitId"])
        exit()

print("All gud")