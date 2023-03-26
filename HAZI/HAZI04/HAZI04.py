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
def did_pre_course(df : dict):
    new_df = df.copy()
    subset = new_df[new_df['test preparation course'] == "completed"]
    return subset


# 5 feladat
def average_scores(df : dict):
    new_df = df.copy()
    df_average = new_df.groupby(['parental level of education'])['math score','reading score','writing score'].mean()
    return df_average


# 6 feladat
def add_age(df : dict):
    new_df = df.copy()  
    np.random.seed(42)  
    new_df['age'] = np.random.randint(18,67,new_df.shape[0])
    return new_df


# 7 feladat
def female_top_score(df : dict):
    new_df = df.copy()
    top_score = 0
    for i in range(len(new_df)):
        if new_df['gender'][i] == 'female' and (new_df['math score'][top_score]+new_df['writing score'][top_score]+new_df['reading score'][top_score]) < (new_df['math score'][i] + new_df['writing score'][i] + new_df['reading score'][i]):
            top_score = i
    return (new_df['math score'][top_score],new_df["reading score"][top_score],new_df["writing score"][top_score])


# 8 feladat
def add_grade(df : dict):
    new_df = df.copy()
    new_df['grade'] = ''
    for i in range(len(new_df)):
        perc = ((new_df['math score'][i] + new_df['reading score'][i] + new_df['writing score'][i]) / 300)
        if perc < 0.6:
            new_df['grade'][i] = 'F'
        elif perc >= 0.6 and perc < 0.7:
            new_df['grade'][i] = 'D'
        elif perc >= 0.7 and perc < 0.8:
            new_df['grade'][i] = 'C'
        elif perc >= 0.8 and perc < 0.9:
            new_df['grade'][i] = 'B'
        elif perc >= 0.9:
            new_df['grade'][i] = 'A'
    return new_df


# 9 feladat
def math_bar_plot(df : dict):
    new_df = df.copy()
    fig,ax = plt.subplots()
    df_groupped = new_df.groupby('gender')['math score'].mean()
    ax.bar(df_groupped.index,df_groupped.values)
    ax.set_ylabel('Math Score')
    ax.set_xlabel('Gender')
    ax.set_title('Average Math Score by Gender')
    return fig


# 10 feladat
def writing_hist(df : dict):
    new_df = df.copy()
    fig,ax = plt.subplots()
    ax.hist(new_df['writing score'])
    ax.set_ylabel('Number of Students')
    ax.set_xlabel('Writing Score')
    ax.set_title('Distribution of Writing Scores')
    return fig


# 11 feladat
def ethnicity_pie_chart(df : dict):
    new_df = df.copy()
    fig,ax = plt.subplots()
    df_groupped = new_df.groupby(['race/ethnicity'])['race/ethnicity'].count()
    ax.set_title('Proportion of Students by Race/Ethnicity')
    ax.pie(df_groupped,labels = df_groupped.index,autopct='%1.1f%%')
    return fig
























