import pandas as pd
import statsmodels.api as sm
import Clean


low_memory=False


df = pd.read_csv('unzipped_data/Train.csv')
testdf = pd.read_csv('./unzipped_data/test.csv')

df = Clean.clean(df)
testdf = Clean.clean(testdf)

#model one
X_train = df[['WL','SSL','BL','TTT','MG']]
y_train = df['SalePrice']
X_train = sm.add_constant(X_train)

model = sm.OLS(y_train, X_train)
result = model.fit()

X_test = testdf[['WL','SSL','BL','TTT','MG']]
X_test = sm.add_constant(X_test)

testdf['SalePrice'] = result.predict(X_test)
testdf[['SalesID', 'SalePrice']].to_csv('model1.csv', index=False, sep=',')


#model2 with age
features = ['WL','SSL','BL','TTT','MG','Age']
X_train = df[features]
X_test = sm.add_constant(X_test)

model2 = sm.OLS(y_train, X_train)
result2 = model2.fit()
X_test = testdf[features]


testdf['SalePrice'] = result.predict(X_test)
testdf[['SalesID', 'SalePrice']].to_csv('model2.csv', index=False, sep=',')




