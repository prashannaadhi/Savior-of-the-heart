# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

''' def dataEntry():
    #     # INITIAL DATA ENTRY BY USER
    #     sex = input('Enter Your Gender (m=0/f=1) ')
    #     age = input('Enter your Age(18-60) ')
    #     SBD = input('What is your SBD( ) ')
    #     TOH = input('Done treatment for hypertension(0/1) ')
    #     smoke = input('Are you current smoker(0/1) ')
    #     diabetes = input('Do you have Diabetes(0/1)')
    #     HDL = input('What is your HDL level ( ) ')
    #     TCL = input('What is your TCL level ( ) ')
    #     print(sex, age, SBD, TOH, smoke, diabetes, HDL, TCL)
    #     return [[sex, age, SBD, TOH, smoke, diabetes, HDL, TCL]]
'''

#def SVR(sex, age, SBP, TOH, smoke , diabetes, HDL, TDL):
# importing the dataset
dataset = pd.read_csv('dataset_savioroftheheart.csv')
X = dataset.iloc[:, :-2].values
y = dataset.iloc[:, 9].values

# Categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_C = LabelEncoder()
X[:, 0] = labelencoder_C.fit_transform(X[:, 0])
X[:, 3] = labelencoder_C.fit_transform(X[:, 3])
X[:, 4] = labelencoder_C.fit_transform(X[:, 4])
X[:, 5] = labelencoder_C.fit_transform(X[:, 5])
onehotencoder = OneHotEncoder(categorical_features=[0, 3, 4, 5])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the dummy variable trap
X_adum = X[:, [1, 3, 5, 7, 8, 9, 10, 11]]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_adum, y, test_size=0.2)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
#X_test = [[1, 1, 1,0,31,120 ,45, 220]]

# Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X_train, y_train)

# Predicting a new result
y_pred = regressor.predict(X_test)
# y_pred = regressor.predict([[sex, age, SBP, TOH, smoke, diabetes, HDL, TDL]])
'''
# Returns the coefficient of determination R^2 of the prediction.
from sklearn.metrics import r2_score

print("R2 cofficient is")
print(r2_score(y_test, y_pred))


# finding Total Error
def errorPER(test, pred):
    error = 0
    for x in range(len(test)):
        tempError = abs(test[x] - pred[x]) / test[x]
        tempError = tempError * 100
        error = error + tempError
    avg = error / len(test)
    print("avg Error ")
    print(avg)
    print("avg Accuracy ")
    print(100 - avg)


errorPER(y_test, y_pred)

# calculating point density
# xy = np.vstack([Y_plot, y_pred])
# z = gaussian_kde(xy)(xy)
# plt.scatter(Y_plot, y_pred, c=z, label='data', marker='o')

plt.scatter(y_test, y_pred, c=range(len(y_test)), label='data', marker='o')
plt.plot(y_pred, y_pred, color='blue')
plt.title('Saviour of Heart(SVR)')
plt.xlabel('Testing value')
plt.ylabel('Prediction')
plt.show() 

print(y_pred)
'''