import pandas as pd
import numpy as np
#400,000 rows
#5,000 model ID


def clean(df):
    df['Age'] = 2016 - df['YearMade'] #this creates the Age column, current year (2016) - Year Made
    df = df[df['Age'] < 900] #drop less than 1000
    #df['Coupler_System'] = pd.get_dummies(df['Coupler_System'])['Yes']



    #creates categorical values for 6 different product groups
    #sets baseline of variable 'TEX' as our most frequently sold type
    prod_groups = pd.get_dummies(df['ProductGroup']).drop('TEX', axis=1)
    #adds variables to end of dataframe
    df = pd.concat([df, prod_groups], axis=1)

    return (df)

