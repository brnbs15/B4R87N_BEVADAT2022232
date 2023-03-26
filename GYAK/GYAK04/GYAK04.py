import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


stats = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }




# 1 feladat
def dict_to_dataframe(dataframe :dict) -> pd.core.frame.DataFrame:
    new_df = dataframe.copy() 
    df=pd.DataFrame(new_df)
    return df




# 2 feladat
def get_column(dataframe :dict,input_string : str) -> pd.core.frame.DataFrame:
    new_df = dataframe.copy() 
    df=pd.DataFrame(new_df)
    return df[f"{input_string}"]





# 3 feladat
def get_top_two(dataframe : pd.core.frame.DataFrame) ->  pd.core.frame.DataFrame:
    new_df = dataframe.copy() 
    df=pd.DataFrame(new_df)
    df_filtered=df.sort_values("area", ascending=False)
    return df_filtered[:2]


# 4 feladat
def population_density(dataframe : pd.core.frame.DataFrame) ->  pd.core.frame.DataFrame:
    new_df = dataframe.copy() 
    df=pd.DataFrame(new_df)
    df["Density"]=df["area"]+df["population"]
    df_pop=df
    df_pop["Density"]=df["population"]/df["area"]
    return df_pop


# 5 feladat
def plot_population(dataframe : pd.core.frame.DataFrame) -> plt.figure:
    new_df = dataframe.copy() 
    df=pd.DataFrame(new_df)
    x=np.array(df["country"])
    y=np.array(df["population"])
    fig,ax=plt.subplots()
    barplot= ax.bar(x,y)
    ax.set_xlabel('Country')
    ax.set_ylabel("Population (millions)")
    ax.set_title("Population of Countries")
    return fig



# 6 feladat
def plot_area( dataframe : pd.core.frame.DataFrame) -> plt.figure:
    new_df = dataframe.copy() 
    df=pd.DataFrame(new_df)
    mylabels=np.array(df["country"])
    x=np.array(df["population"])
    fig,ax=plt.subplots()
    barplot= ax.pie(x,labels=mylabels)
    ax.set_title("Area of Countries")
    return fig



