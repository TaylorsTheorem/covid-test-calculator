
''' Class for objects containing all important information about each district '''

class District:

    def __init__(self, data):
        self.name = data["Name"]
        self.id = data["AdmUnitId"]

        self.total_cases = data["AnzFall"]
        self.total_deaths = data["AnzTodesfall"]
        self.total_recovered = data["AnzGenesen"]
        self.total_active = data["AnzAktiv"]

        self.new_cases = data["AnzFallNeu"]
        self.new_deaths = data["AnzTodesfallNeu"]
        self.new_recovered = data["AnzGenesenNeu"]
        self.new_active = data["AnzAktivNeu"]

        self.week_cases = data["AnzFall7T"]

        self.incidence = data["Inz7T"]