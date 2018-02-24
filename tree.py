# Decision Tree Problem Skeleton Code: 


# For this problem, you can refer to: 
# http://scikit-learn.org/stable/modules/tree.html and
# http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier

# Some of the libraries you might need are loaded:
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import hamming_loss
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

# Feel free to use other libraries.

data = np.genfromtxt('wbdc.txt', delimiter=',') # wdbc is loaded into an array 'data'


# PART ONE:
Num_err1 = []
Num_err2 = []
size = [50, 100, 150, 200, 250, 300, 350, 400, 450]
for dp in range(2,4):
    for sz in size:
        train, test = data[1:sz+1, :], data[sz+1:, :] # divide data into training and test sets
        X_trn, y_trn = train[:, 2:], train[:,1] # separate the features and labels of training
        X_tst, y_tst = test[:, 2:], test[:,1] # separate the features and labels of test

        # Compute the training and test errors for depth = 2, and plot them as a function of sz
        # Compute the training and test errors for depth = 3, and plot them as a function of sz

        # CODE GOES HERE (YOU CAN USE THE SKLEARN DECISION TREES)
        clf = DecisionTreeClassifier(max_depth=dp)
        x_fit = clf.fit(X_trn, y_trn)
        x_pred_train = x_fit.predict(X_trn)
        x_pred_test = x_fit.predict(X_tst)

        error_test = (y_tst != x_pred_test).sum()
        error_train = (y_trn != x_pred_train).sum() 
        errorRate_test = error_test/y_tst.size 
        errorRate_train = error_train/y_trn.size

        Num_err1.append(errorRate_test)
        Num_err2.append(errorRate_train)
        
    plt.figure(dp-1)
    plt.plot(size, Num_err1, 'r', size, Num_err2, 'b')
    Num_err1=[]
    Num_err2=[]
# You will have a total of two plots for this part (one for each depth)

size = [200, 400]
i=2
for sz in size:
    train, test = data[1:sz+1, :], data[sz+1:, :] # divide data into training and test sets
    X_trn, y_trn = train[:, 2:], train[:,1] # separate the features and labels of training
    X_tst, y_tst = test[:, 2:], test[:,1] # separate the features and labels of test
    
    # Train decision trees of maximum depth = 2,...,12 using the training set using IG criterion.
    # Plot the training and test error as a function of the depth.
    # Repeat the above using gini index
    
    # CODE GOES HERE 
    
    criter =['entropy','gini']
#     for crt in criter:
    for depth in range(2,13):
        clf = DecisionTreeClassifier(criterion='gini', max_depth=depth)
        x_fit = clf.fit(X_trn, y_trn)
        x_pred_train = x_fit.predict(X_trn)
        x_pred_test = x_fit.predict(X_tst)

        error_test = (y_tst != x_pred_test).sum()
        error_train = (y_trn != x_pred_train).sum() 
        errorRate_test = error_test/y_tst.size 
        errorRate_train = error_train/y_trn.size

        Num_err1.append(errorRate_test)
        Num_err2.append(errorRate_train)
    i=i+1    
    plt.figure(i)
    plt.plot(range(2,13), Num_err1, 'r', range(2,13), Num_err2, 'b')
    Num_err1=[]
    Num_err2=[]   
        
    for depth in range(2,13):
        clf = DecisionTreeClassifier(criterion='entropy', max_depth=depth)
        x_fit = clf.fit(X_trn, y_trn)
        x_pred_train = x_fit.predict(X_trn)
        x_pred_test = x_fit.predict(X_tst)

        error_test = (y_tst != x_pred_test).sum()
        error_train = (y_trn != x_pred_train).sum() 
        errorRate_test = error_test/y_tst.size 
        errorRate_train = error_train/y_trn.size

        Num_err1.append(errorRate_test)
        Num_err2.append(errorRate_train)
    i=i+1    
    plt.figure(i)
    plt.plot(range(2,13), Num_err1, 'r', range(2,13), Num_err2, 'b')
    Num_err1=[]
    Num_err2=[]
#   lable=, marker = o,      
        
        
# You will have a total of four plots for this part (2 training sets and two decision criteria)


# PART 3: We will use minimum leaf size, which ensures that each node must have at least a certain number of samples
size = [50, 200, 400]
for sz in size:
    train, test = data[1:sz+1, :], data[sz+1:, :] # divide data into training and test sets
    X_trn, y_trn = train[:, 2:], train[:,1] # separate the features and labels of training
    X_tst, y_tst = test[:, 2:], test[:,1] # separate the features and labels of test
    
    # Train decision trees with minimum leaf size = 1, 2,..., 15 using the training set using IG criterion.
    # Plot the training and test error as a function of the depth.
    # Repeat the above using gini index
    
    # CODE GOES HERE 
    for msl in range(1,16):
        clf = DecisionTreeClassifier(criterion='entropy',min_samples_leaf=msl,random_state = 0)
        x_fit = clf.fit(X_trn, y_trn)
        x_pred_train = x_fit.predict(X_trn)
        x_pred_test = x_fit.predict(X_tst)

        error_test = (y_tst != x_pred_test).sum()
        error_train = (y_trn != x_pred_train).sum() 
        errorRate_test = error_test/y_tst.size 
        errorRate_train = error_train/y_trn.size

        Num_err1.append(errorRate_test)
        Num_err2.append(errorRate_train)

    i=i+1    
    plt.figure(i)
    plt.plot(range(1,16), Num_err1, 'r', range(1,16), Num_err2, 'b')
    Num_err1=[]
    Num_err2=[]
# You will have a total of three plots for this part


# Please justify the plots. You may want to use random_state= 0 or some small integer in the sklearn. 


