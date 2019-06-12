import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def random_forest(sex, age, SBP, TOH, smoke , diabetes, HDL, TDL):

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
    
    # splitting the data set into training set and testing set
    from sklearn.model_selection import train_test_split
    
    X_train, X_test, y_train, y_test = train_test_split(X_adum, y, test_size=0.2, random_state=0)
    
    '''
    #Perform grid search
    gsc = GridSearchCV(estimator = RandomForestRegressor(),param_grid = {
            'max_depth': range(3,7),'n_estimators':(10,50,100,1000),},
            cv = 5, scoring = 'neg_mean_squared_error', verbose = 0, n_jobs = -1)
    grid_result = gsc.fit(X_adum,y)
    '''
    # fitting random forest regression to the training set
    from sklearn.ensemble import RandomForestRegressor
    
    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    regressor.fit(X_train, y_train)
    '''
    from sklearn.ensemble import RandomForestRegressor
    rfr = RandomForestRegressor(max_depth = [3,4,5,6,7],
                                n_estimators = [10,50,100,1000], 
                                random_state = False, verbose = False)
    scores = cross_val_predict(rfr,X_adum,y,cv = 10)
    '''
    y_pred = regressor.predict([[1, 1, 1,0,31,120 ,45, 220]])
    # pr.edicting the test set results
    # y_pred = regressor.predict(X_test)
    print(y_pred)
    # y_feature = regressor.feature_importances_
    
    # percisoin
    '''test=list(y_test.astype(int))
    pred=list(y_pred.astype(int))
    from sklearn.metrics import precision_recall_fscore_support as score
    precision,recall, fscore, support = score(y_test, y_pred,average='weighted')
    fscore= score(y_test, y_pred)
    print('precision: {}'.format(precision))
    print('recall: {}'.format(recall))
    print('fscore: {}'.format(fscore))
    print('support: {}'.format(support))'''
    
    '''# Returns the coefficient of determination R^2 of the prediction.
    from sklearn.metrics import r2_score
    
    print("R2 cofficient is")
    print(r2_score(y_test, y_pred))
    
    # average error of our model
    def error(test, pred):
        error = 0
        for x in range(len(test)):
            temperror = abs(test[x] - pred[x]) / test[x]
            temperror = temperror * 100
            error = error + temperror
        avg = error / len(test)
        print("avg Error ")
        print(avg)
        print("avg Accuracy ")
        print(100 - avg)
    
    
    error(y_test, y_pred)
    
    # plotting
    plt.scatter(y_test, y_pred, c=range(len(y_pred)))
    plt.plot(y_test, y_test, color='k')
    plt.xlabel('Actual risk score')
    plt.ylabel('Predicted risk score')
    plt.show()'''
    
    return(y_pred)

