from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df=pd.read_csv('Salary_dataset.csv')

del df['Unnamed: 0']
df.dropna(inplace=True)

feature=df['YearsExperience'].values.reshape(-1, 1)
label=df['Salary']

train_feature, test_feature, train_label, test_label=train_test_split(feature, label)

model=LinearRegression()
model.fit(train_feature, train_label)

prediction=model.predict(test_feature)

print("Mean Absolute Error:", mean_absolute_error(test_label, prediction))
print("Mean Squared Error:", mean_squared_error(test_label, prediction))
print("R2 Score", r2_score(test_label, prediction))

import joblib
import os

if os.path.exists('salary_predictor.pkl'): os.remove('salary_predictor.pkl')
joblib.dump(model, 'salary_predictor.pkl')