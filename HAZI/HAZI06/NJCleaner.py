import pandas as pd

class NJCleaner():
    
    
    
    def __init__(self,path):
        self.data= pd.read_csv(path)

    def  order_by_scheduled_time(self):
        ordered=self.data.sort_values(by="scheduled_time")
        return ordered
    def drop_columns_and_nan(self):
        self.data.drop(columns=["from","to"])
