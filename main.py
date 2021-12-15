import json
import districts
from gui import Gui

''' Main running module '''

# Method to load data.txt
def get_data():
    with open("data.txt", "r") as datafile:
        return json.loads(datafile.read())

# Start main
def main():

    # Save data and district_list
    data = get_data()
    district_list = [districts.District(val) for val in data]
    Gui(1400,400,district_list)


# Init
if __name__ == "__main__":
    main()