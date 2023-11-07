import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
import sklearn.metrics as metrics
from sklearn.metrics import ConfusionMatrixDisplay
def logistic_regression():
    df = pd.read_csv('train.csv')
    y = df['price_range']
    X = df.drop('price_range', axis = 1)

    # Split the data into test and train by using sklearn.
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.25)

    # 42 is the Answer to the Ultimate Question of Life...
    lr = LogisticRegression(random_state = 42, max_iter=100000)
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred_lr)
    print("Logistic Regression has Etest accuracy:" + str(accuracy))
    ConfusionMatrixDisplay.from_predictions(y_test,y_pred_lr)
#     print_my_confusion_matrix(metrics.confusion_matrix(y_test, y_pred_lr))

    
logistic_regression()

def k_neighbors():
    df = pd.read_csv('train.csv')
    y = df['price_range']
    X = df.drop('price_range', axis = 1)

    # Split the data into test and train by using sklearn.
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.25)

    model = KNeighborsClassifier()
    model.fit(X_train,y_train)
    predicted= model.predict(X_test)

    accuracy = metrics.accuracy_score(y_test,predicted)
    print("K-neighbors has Etest accuracy:" + str(accuracy))
    ConfusionMatrixDisplay.from_predictions(y_test,predicted)


k_neighbors()

def decision_tree():
    df = pd.read_csv('train.csv')
    y = df['price_range']
    X = df.drop('price_range', axis = 1)

    # Split the data into test and train by using sklearn.
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.25)

    first_tree = DecisionTreeClassifier()
    first_tree.fit(X_train, y_train)
    y_pred=first_tree.predict(X_test)
    accuracy = metrics.accuracy_score(y_test,y_pred)
    print("Decision Tree has Etest accuracy:" + str(accuracy))
    ConfusionMatrixDisplay.from_predictions(y_test,y_pred)

decision_tree()
    
