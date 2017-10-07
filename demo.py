import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

#read data
datafram = pd.read_fwf('bain_body.txt')
x_values = datafram[['Brain']]
y_values = datafram[['Body']]

#train model on data
body_reg = linear_model.LinearRegression()
body_red.fit(x_values, y_value)

#visualize results
plt.scatter(x_value, y_value)
plt.plot(x_values, body_red.predict(x_value))
