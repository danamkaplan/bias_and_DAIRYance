import pandas as pd
import Clean


import pandas as pd
low_memory=False


df = pd.read_csv('unzipped_data/Train.csv')

df = Clean.clean(df)

#modeling stuff with df
