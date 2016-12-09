#400,000 rows
#5,000 model ID


def clean(df):
    df['Age'] = 2016 - df['YearMade'] #this creates the Age column, current year (2016) - Year Made

    df['Couple_System'] = pd.get_dummies(df['Coupler_System'])['Yes']

    return (clean_df)
