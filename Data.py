import csv
from Patient import Patient

class Data:
    """Data class."""

    def __init__(self,file_name,start,end):
        self.dates = []
        self.data = []
        with open(file_name) as file:
            reader = csv.reader(file,delimiter=',')
            self.header = next(reader)
            previousDate = "foo"
            for row in reader:
                date = row[0]
                if (date<start): continue ;
                if (date>end): break ;
                patient = Patient(self.header,row)
                if not(date==previousDate):
                    self.dates.append(date)
                    today = []
                    self.data.append(today)
                    previousDate = date
                today.append(patient)

    def number_of_days(self): return len(self.dates)

    def dates(self): return self.dates

    def date(self,day): return self.dates[day]

    def day(self,date): return self.dates.index(date)

    def patients(self,day): return self.data[day]

    def number_of_patients(self,day): return len(self.data[day])

    def patient(self,day,patient): return self.data[day][patient]

