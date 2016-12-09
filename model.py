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


model = sm.OLS(y_train, sm.add_constant(X_train))
result = model.fit()

X_test = testdf[['WL','SSL','BL','TTT','MG']]

testdf['SalePrice'] = result.predict(sm.add_constant(X_test))
testdf[['SalesID', 'SalePrice']].to_csv('model1.csv', index=False, sep=',')


#model2 with age
features = ['WL','SSL','BL','TTT','MG','Age']
X_train = df[features]

model2 = sm.OLS(y_train,  sm.add_constant(X_train))
result2 = model2.fit()
X_test = testdf[features]

X_test = testdf[features]

testdf['SalePrice'] = result2.predict(sm.add_constant(X_test))
testdf[['SalesID', 'SalePrice']].to_csv('model2.csv', index=False, sep=',')


#model3 with only age
features = 'Age'
X_train = df[features]

model3 = sm.OLS(y_train, sm.add_constant(X_train))

result3 = model3.fit()

X_test = testdf[features]

testdf['SalePrice'] = result3.predict(sm.add_constant(X_test))
testdf[['SalesID', 'SalePrice']].to_csv('model3.csv', index=False, sep=',')

#model3 with only age
features = ['WL','SSL','BL','TTT','MG','Age']
X_train = df[features]

model3 = sm.OLS(y_train, sm.add_constant(X_train))

result3 = model3.fit()

X_test = testdf[features]

testdf['SalePrice'] = result3.predict(sm.add_constant(X_test))
testdf[['SalesID', 'SalePrice']].to_csv('model3.csv', index=False, sep=',')




