#400,000 rows
#5,000 model ID

import pandas as pd
low_memory=False

df = pd.read_csv('unzipped_data/Train.csv')



df['Age'] = 2016 - df['YearMade'] #this creates the Age column, current year (2016) - Year Made
