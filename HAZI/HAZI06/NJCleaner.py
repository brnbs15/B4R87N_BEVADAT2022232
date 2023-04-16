import pandas as pd
from datetime import datetime

class NJCleaner():
    
    
    def __init__(self,path):
        self.data= pd.read_csv(path)

    def  order_by_scheduled_time(self):
        ordered=self.data.sort_values(by="scheduled_time")
        return ordered
    
    def drop_columns_and_nan(self):
        self.data.drop(columns=["from","to"])
    
    def convert_date_to_day(self):
        dates=pd.array(self.data["date"])
        for item in dates:
            datum=datetime.strptime(item,"%Y-%m-%d")
            self.data = self.data.replace([item], datum.strftime("%A"))
        return self.data


path="C:/Tanulas/MI_specializáció/bevadat/files/2018_03.csv"
njcleaner=NJCleaner(path)
njcleaner.convert_date_to_day()      
print(njcleaner.data)
