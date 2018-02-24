# Gaussian Naive Bayes Skeleton Code: 

import numpy as np
import math 
from sklearn.metrics import hamming_loss
import matplotlib.pyplot as plt

from scipy.stats import norm

def Gau_Cla(x, mean, var):
    temp = ((x - mean)** 2) / var
    return (1 / math.sqrt(2 * math.pi * var)) * math.exp(-1/2 * temp)

data = np.genfromtxt('wbdc.txt', delimiter=',')

size = [50, 100, 150, 200, 250, 300, 350, 400, 450]
train_error = []
test_error = []
for sz in size:
    train, test = data[1:sz+1, :], data[sz+1:, :]
    X_trn, y_trn = train[:, 2:], train[:,1]
    X_tst, y_tst = test[:, 2:], test[:,1]
    
    # Compute the label probabilities
    num_benign = 0
    for y in y_trn:
        if y == 1:
            num_benign += 1
            
    prob_benign = num_benign / len(y_trn)
    num_mal = len(y_trn) - num_benign
    prob_malignant = num_mal / len(y_trn)
    
    # Compute the class conditional means, and variance for Gaussian Naive Bayes
    # You 'may' obtain four arrays/lists of size 30, two for means for each label, 
    # and two for variances for each label. 
    
    b_mean = [0] * 30
    m_mean = [0] * 30
    b_var = [0] * 30
    m_var = [0] * 30
    
    # x should represent the array for each patient
    for i in range(0, 30):
        for j in range(0, len(y_trn)):
            # If it is benign == 1
            if (y_trn[j] == 1):
                b_mean[i] += X_trn[j][i]
            else:
                m_mean[i] += X_trn[j][i]
            
    for i in b_mean:
        i = i / num_benign
    for i in m_mean:
        i = i / num_mal
    
    for i in range(0, 30):
        for j in range(0, len(y_trn)):
            if y_trn[i] == 1:
                b_var += (X_trn[j][i] - b_mean) ** 2
            else:
                m_var += (X_trn[j][i] - m_mean) ** 2
                
    for i in b_var:
        i = i / num_benign
    for i in m_var:
        i = i / num_mal
    
    # Training error
    train_result = []
    for i in range(0, len(y_trn)):
        ben_out = prob_benign
        mal_out = prob_malignant
        for j in range(0, 30):
            ben = Gau_Cla(X_trn[i][j], b_mean[j], b_var[j])
            ben_out *= ben
            mal = Gau_Cla(X_trn[i][j], m_mean[j], m_var[j])
            mal_out *= mal
        
        if ben_out >= mal_out:
            train_result.append(1)
        else:
            train_result.append(0)
            
    error = 0
    for i in range(0, len(y_trn)):
        if train_result[i] != y_trn[i]:
            error += 1
    error = error / len(y_trn)
    train_error.append(error)

    # Testing
    test_result = []
    for i in range(0, len(y_tst)):
        ben_out = prob_benign
        mal_out = prob_malignant
        for j in range(0, 30):
            ben = Gau_Cla(X_tst[i][j], b_mean[j], b_var[j])
            ben_out *= ben
            mal = Gau_Cla(X_tst[i][j], m_mean[j], m_var[j])
            mal_out *= mal

        if ben_out >= mal_out:
            test_result.append(1)
        else:
            test_result.append(0)
            
    error = 0
    for i in range(0, len(y_tst)):
        if test_result[i] != y_tst[i]:
            error += 1
    error = error / len(y_tst)
    test_error.append(error)
    
plt.plot(train_error, 'r', test_error, 'b')
plt.show()
