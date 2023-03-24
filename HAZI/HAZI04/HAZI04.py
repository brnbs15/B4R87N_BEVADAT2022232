import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# 1 feladat
def csv_to_df( path : str) -> pd.core.frame.DataFrame:
    df=pd.read_csv(path)
    print(df)
    return df
#df=csv_to_df("C:/Tanulas/MI_specializáció/bevadat/files/StudentsPerformance.csv")

# 2 feladat
def capitalize_columns(df : dict) -> pd.core.frame.DataFrame:
    new_df = df.copy()
    heads=list(new_df.head())
    for i in range(len(heads)):
        if "e" not in heads[i]:
            heads[i]=heads[i].upper()
    print(heads)
    new_df.columns=heads
    print(new_df)
    return new_df

# 3 feladat
def math_passed_count(df : dict) -> int:
    new_df = df.copy()
    scores=new_df.__getitem__("math score")
    counter=0
    for item in scores:
        if item > 50:
            counter += 1
    return counter

# 4 feladat

#def did_pre_course(df : dict) -> pd.core.frame.DataFrame:
    #new_df = df.copy()



# 5 feladat



# 6 feladat


# 7 feladat


# 8 feladat

# 9 feladat




# 10 feladat




# 11 feladat




# 12 feladat