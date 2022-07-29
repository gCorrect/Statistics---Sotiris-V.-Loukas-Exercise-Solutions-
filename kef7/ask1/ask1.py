import pandas as pd
from sklearn import linear_model

data = {
  "mathematics": [5,6,4,10,9,7,8],
  "greek": [7,6,9,5,3,4,8]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

X = df[['mathematics']]
y = df['greek']

regr = linear_model.LinearRegression()
regr.fit(X, y)


#predict the CO2 emission of a car where the weight is 2300g, and the volume is 1300ccm:
prediction = regr.predict([[3]])
text= "predicted greek: "
print(text)
print(  prediction)
print(  regr.coef_) # coeffient

