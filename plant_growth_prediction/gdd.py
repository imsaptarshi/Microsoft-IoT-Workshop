import csv
import math

FILE="data.csv"
FIELDS=["date","temperature"]

class GDD:
    def __init__(self,required_gdd:int,base_temperature:float):
        self.required_gdd=required_gdd
        self.base_temperature=base_temperature
    
    def calculate_gdd_received(self):#gdd received_per_day
        min=100
        max=0
        with open(FILE) as csv_file:
            dict_reader=csv.DictReader(csv_file)
            for row in dict_reader:
                temp=row["temperature"]

                if float(temp)<min:
                    min=float(temp)

                if float(temp)>max:
                    max=float(temp)

        self.gdd=math.ceil((max+min)/2 - self.base_temperature)
        return self.gdd

    def predict_number_of_days(self):
        return math.ceil(self.required_gdd/self.gdd)


if __name__=="__main__":
    #example
    corn=GDD(400,10)
    print(corn.calculate_gdd_received())
    print(corn.predict_number_of_days())