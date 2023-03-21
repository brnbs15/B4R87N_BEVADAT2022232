import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


stats = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }




# 1 feladat
def dict_to_dataframe(stats :dict) -> pd.core.frame.DataFrame:
    df=pd.DataFrame(stats)
    return df

dict_to_dataframe(stats)




# 2 feladat
def dict_to_dataframe(stats :dict,input_string : str) -> pd.core.frame.DataFrame:
    df=pd.DataFrame(stats)
    print(df[f"{input_string}"])
    return df[f"{input_string}"]
dict_to_dataframe(stats,"area")




# 3 feladat
df=pd.DataFrame(stats)
def get_top_two(stats : pd.core.frame.DataFrame) ->  pd.core.frame.DataFrame:
    df_filtered=df.sort_values("area", ascending=False)
    return df[:2]
get_top_two(df)


# 4 feladat
def population_density(stats : pd.core.frame.DataFrame) ->  pd.core.frame.DataFrame:
    df["Density"]=df["area"]+df["population"]
    df_pop=df
    for i in range(len(df)):
        df_pop["Density"][i]=df["population"][i]/df["area"][i]
    print(df_pop)
    return df_pop
population_density(stats)


