import pandas as pd
import numpy as np
df = pd.read_csv('heart.csv')
df
x=df.drop(['output'], axis=1)
x
y=df['output']
y

from sklearn.preprocessing import MinMaxScaler
scaled = MinMaxScaler()

x_scaled = scaled.fit_transform(x)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x_scaled,y,random_state=42,test_size=0.25)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
y_pred

from sklearn.metrics import ConfusionMatrixDisplay,accuracy_score,classification_report
ConfusionMatrixDisplay.from_predictions(y_test,y_pred)

accuracy_score(y_test,y_pred)*100

print(classification_report(y_test,y_pred))
